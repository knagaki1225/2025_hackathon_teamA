from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from .forms import ImageUploadForm
from django.contrib.auth import get_user_model
from .models import User
from django.contrib.auth import views as auth_views


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
    
class HomeView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = [
            {
                "id": 1,
                "name": "Java",
                "subcategories": [
                    {"name": "Java基礎"},
                    {"name": "Java応用"},
                ]
            },
            {
                "id": 2,
                "name": "Python",
                "subcategories": [
                    {"name": "Python基礎"},
                    {"name": "Python応用"},
                ]
            }
        ]
        context['categories'] = categories
        return context

class SubcategoryDetailView(View):
    def get(self, request, subcategory_name):
        subcategory = {
            "name": subcategory_name,
            "description": f"{subcategory_name} の詳細です。",
        }
        return render(request, 'category/subcategory.html', {'subcategory': subcategory})

class CustomPasswordResetView(auth_views.PasswordResetView):
    template_name = 'account/password_reset.html'
    email_template_name = 'account/password_reset_email.html'
    subject_template_name = 'accounts/password_reset_subject.txt'
    success_url = reverse_lazy('account:password_reset_done')

class CustomPasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'

class CustomPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    success_url = reverse_lazy('account:password_reset_complete')

class CustomPasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'
