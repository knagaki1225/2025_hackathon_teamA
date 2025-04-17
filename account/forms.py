from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['icon_url']  # ユーザーのアイコンのみをアップロード対象にする

class AccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['language', 'career', 'my_ditail']
