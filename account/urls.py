from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'), # サインアップページ
    path('upload-icon/', views.upload_icon, name='upload_icon'),  # 画像アップロードページ
    path('all/', views.AllView.as_view(), name='all'),
    path('admin/<int:pk>', views.AccountsDetailView.as_view(), name='accountsDetail'),
]
