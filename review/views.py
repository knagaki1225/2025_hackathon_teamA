from django.shortcuts import render
from django.views import generic    # 汎用ビューのインポート
from .models import Review
from django.db.models import Count, Q

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