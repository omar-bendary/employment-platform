from django.urls import path
from .views import ProfileListView, SignUpView, ProfileDetail

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile_list/', ProfileListView.as_view(), name='profile_list'),
    path('profile/<int:pk>/', ProfileDetail.as_view(), name='profile_detail'),
]
