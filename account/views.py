# accounts/views.py
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from .forms import ImageUploadForm
from django.contrib.auth import get_user_model
from .models import User

User = get_user_model()

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
    
@login_required  # ログインユーザーのみがアクセスできるようにする
def upload_icon(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            user.icon_url = form.cleaned_data['icon_url']
            user.save()  # ユーザーのアイコンを保存
            return redirect('profile')  # アップロード後にリダイレクト(遷移先は適宜変更)
    else:
        form = ImageUploadForm()

    return render(request, 'accounts/upload_icon.html', {'form': form})

class AllView(generic.ListView):
    model = User
    template_name = 'accounts/all.html'

class AccountsDetailView(generic.DetailView):
    model = User
    template_name = 'accounts/detail.html'
