from django.shortcuts import render
from django.views import generic    # 汎用ビューのインポート
from .models import Review, Class
from django.db.models import Count, Q, Avg

def search():
    render

def review_list(request):
    reviews = Review.objects.annotate(
        good_count=Count('good', filter=Q(good__del_flg=False))
    ).order_by('-good_count')

    return render(request, 'home.html', {'reviews': reviews})

class ReviewDetailView(generic.DetailView):
    model = Review
    template_name = 'review/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        review = self.get_object()

        # 対象クラス
        target_class = review.class_id

        # del_flg=False のレビューのみ取得
        related_reviews = Review.objects.filter(
            class_id=target_class,
            del_flg=False
        )

        # 平均レビュー点数も del_flg=False で絞る
        avg_review = related_reviews.aggregate(avg=Avg('review_num'))['avg']

        # コンテキストに追加
        context['class_info'] = target_class
        context['related_reviews'] = related_reviews
        context['avg_review_num'] = avg_review

        return context
