from django.urls import path
from . import views

app_name = 'review'

urlpatterns = [
    path('', views.review_list, name='index'),  #一覧ページのビュー
    path('<int:pk>/', views.ReviewDetailView.as_view(), name='detailReview'),
    path('search/', views.search, name='search'),
]