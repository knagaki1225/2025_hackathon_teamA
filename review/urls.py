from django.urls import path
from . import views

app_name = 'review'

urlpatterns = [
    path('', views.review_list, name='index'),  #一覧ページのビュー
    path('<int:pk>/', views.ReviewDetailView.as_view(), name='detailReview'),
    path('search/', views.search, name='search'),
    path('review/<int:class_id>/create/', views.ReviewCreateView.as_view(), name='createReview'),
    path('toggle_good/', views.toggle_good, name='toggle_good'),
]
