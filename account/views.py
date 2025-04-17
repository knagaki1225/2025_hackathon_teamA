from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.views import View
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, ImageUploadForm, AccountForm
from django.contrib.auth import get_user_model
from .models import User
from django.contrib.auth import views as auth_views
from review.models import Review, Good, Department
from django.contrib.auth.mixins import LoginRequiredMixin


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
            return redirect(reverse('account:accountsDetail', kwargs={'pk': request.user.pk}))  # アップロード後にリダイレクト(遷移先は適宜変更)
    else:
        form = ImageUploadForm()

    return render(request, 'accounts/upload_icon.html', {'form': form})

class AllView(generic.ListView):
    model = User
    template_name = 'account_list/account_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['departments'] = Department.objects.filter(del_flg=False)  # ← ここで学科一覧を追加
        return context

def AccountDetail(request, pk):
    user = get_object_or_404(User, pk=pk)
    review = Review.objects.filter(user_id__in=[pk], del_flg=False).count()
    good = Good.objects.filter(user_id__in=[pk], del_flg=False).count()

    return render(request, 'account_list/account_mypage.html', {'user':user, 'review':review, 'good':good})
    
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
                    {"name": "Java応用(Spring Boot①)"},
                    {"name": "Java応用(Spring Boot②)"},
                ]
            },
            {
                "id": 2,
                "name": "Python",
                "subcategories": [
                    {"name": "Python基礎"},
                    {"name": "Python応用(Django①)"},
                    {"name": "Python応用(Django②)"},
                    {"name": "Python応用(tkinter)"},
                    {"name": "Python応用(教師あり学習)"},
                ]
            },
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
    subject_template_name = 'account/password_reset_subject.txt'
    success_url = reverse_lazy('account:password_reset_done')

class CustomPasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'account/password_reset_done.html'

class CustomPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'account/password_reset_confirm.html'
    success_url = reverse_lazy('account:password_reset_complete')

class CustomPasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'account/password_reset_complete.html'

@login_required
def edit_user(request):
    user = request.user
    if request.method == 'POST':
        form = AccountForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('review:index')
    else:
        form = AccountForm(instance=user)

    return render(request, 'account_list/ACedit_user.html', {'form': form})