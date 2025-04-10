from django.shortcuts import render
from django.views import generic    # 汎用ビューのインポート
from .models import Review

class IndexView(generic.ListView):
    model = Review     
    template_name = 'top.html'    # 使用するテンプレート名を指定