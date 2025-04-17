from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import (
    CustomPasswordResetView, CustomPasswordResetDoneView,
    CustomPasswordResetConfirmView, CustomPasswordResetCompleteView,
)

app_name = 'account'

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'), # サインアップページ
    path('upload-icon/', views.upload_icon, name='upload_icon'),  # 画像アップロードページ
    path('all/', views.AllView.as_view(), name='all'),
    path('<int:pk>', views.AccountDetail, name='accountsDetail'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('edit/', views.edit_user, name='edit_user'),
]
