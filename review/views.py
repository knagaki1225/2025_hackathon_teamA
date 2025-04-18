from django.shortcuts import render
from django.views import generic    # 汎用ビューのインポート
from .models import Review, Class, Category, Reply, Good
from django.db.models import Count, Q, Avg
from .forms import searchForm
from datetime import datetime, timedelta
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from itertools import islice
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404

def search(request):
    result = None
    forms = searchForm(request.GET)

    if forms.is_valid():
        results = None
        result = []
        words = forms.cleaned_data['words']
        review_num = forms.cleaned_data['review_num']
        result_date = forms.cleaned_data.get('result_date')
        good = forms.cleaned_data.get('good')

        if words == '':
            results = Review.objects.all()
        else:
            # Classのnameフィールドにwordsが含まれているClassを取得
            class_ids = Class.objects.filter(class_name__icontains=words).values_list('id', flat=True)
            # Reviewモデルでclass_idが上で取得したclass_idsに含まれるレビューを取得
            results = Review.objects.filter(class_id__in=class_ids)
        
        if review_num:
            results = results.filter(review_num__gte=review_num)
        
        if result_date:
            now = timezone.now()
            result_date = int(result_date)
            ago = now - timedelta(days=result_date)
            results = results.filter(create_at__gte=ago)
        
        if good:
            results = results.annotate(good_count=Count('good', filter=Q(good__del_flg=False))).order_by('-good_count')
        
        for tmp in results:
            good_count = Good.objects.filter(review_id = tmp.id, del_flg = False).count()
            result.append([tmp, good_count])

    categories = Category.objects.filter(del_flg=False).prefetch_related('classes')

    return render(request, 'home.html',{'results':result,'searchForm':forms, 'categories': categories})

@login_required
def review_list(request):
    tmps = Review.objects.annotate(
        good_count=Count('good', filter=Q(good__del_flg=False))
    ).order_by('-good_count')

    reviews = []

    for review in islice(tmps, 3):
        good_count = Good.objects.filter(review_id = review.id, del_flg = False).count()
        tmp = [review, good_count]
        reviews.append(tmp)

    forms = searchForm(request.GET)

    categories = Category.objects.filter(del_flg=False).prefetch_related('classes')
    
    return render(request, 'home.html', {'reviews': reviews,'searchForm':forms,'categories': categories})

class ReviewDetailView(LoginRequiredMixin, generic.DetailView):
    model = Class
    template_name = 'review/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        target_class = self.get_object()

        # del_flg=False のレビューのみ取得
        related_reviews = Review.objects.filter(
            class_id=target_class,
            del_flg=False
        )

        reviews = []

        for review in related_reviews:
            reply = Reply.objects.filter(
                review_id = review.id,
                del_flg = False
            )
            tmp = [review, reply]

            reviews.append(tmp)

        # 平均レビュー点数も del_flg=False で絞る
        avg_review = related_reviews.aggregate(avg=Avg('review_num'))['avg']

        # コンテキストに追加
        context['class_info'] = target_class
        context['reviews'] = reviews
        context['avg_review_num'] = avg_review

        return context

@method_decorator(login_required, name='dispatch')
class ReviewCreateView(View):
    def post(self, request, class_id):
        Review.objects.create(
            user_id=request.user,
            class_id=Class.objects.get(id=class_id),
            review_num=request.POST.get('review_num'),
            comment=request.POST.get('comment', ''),
            anonymity_flg=bool(request.POST.get('anonymity_flg')),
        )
        return redirect('review:detailReview', pk=class_id)

@require_POST
@login_required
def toggle_good(request):
    review_id = request.POST.get("review_id")
    review = get_object_or_404(Review, id=review_id)

    # 既に存在するか確認（del_flg=False のもの）
    good = Good.objects.filter(user_id=request.user, review_id=review, del_flg=False).first()

    if good:
        # 既に「いいね」してる → del_flg を True に
        good.del_flg = True
        good.save()
        liked = False
    else:
        # まだ「いいね」してない → 新しく追加
        Good.objects.create(user_id=request.user, review_id=review)
        liked = True

    # 最新のいいね数をカウント（del_flg=False のみ）
    like_count = Good.objects.filter(review_id=review, del_flg=False).count()

    return JsonResponse({
        "liked": liked,
        "like_count": like_count,
    })
