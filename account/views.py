from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model
from .models import User



User = get_user_model()

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

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

