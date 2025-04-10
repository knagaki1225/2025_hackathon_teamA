from django.shortcuts import render
from django.views import generic    # 汎用ビューのインポート
from .models import Review

def search():
    render

class IndexView(generic.ListView):
    model = Review     
    template_name = 'top.html'    # 使用するテンプレート名を指定

class ReviewDetailView(generic.DetailView):
    model = Review
    template_name = 'review/detail.html'