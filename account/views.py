# accounts/views.py
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