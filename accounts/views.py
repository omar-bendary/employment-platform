from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from hitcount.views import HitCountDetailView
from accounts.models import Profile
from .forms import CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class ProfileListView(LoginRequiredMixin, ListView):
    model = Profile
    template_name = 'accounts/profile_list.html'
    context_object_name = 'profile_list'


class ProfileDetail(LoginRequiredMixin, HitCountDetailView):
    model = Profile
    template_name = 'accounts/profile_detail.html'
    count_hit = True
