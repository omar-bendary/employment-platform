from django.urls import path
from .views import JobListView, JobDetailView, ApplyView, JobCreateView, SearchResultsListView

urlpatterns = [
    path('', JobListView.as_view(), name='job_list'),
    path('new/', JobCreateView.as_view(), name='new_job'),
    path('job/<int:pk>/', JobDetailView.as_view(), name='job_detail'),
    path('job/<int:pk>/apply', ApplyView.as_view(), name='job_apply'),
    path('search/', SearchResultsListView.as_view(),
         name='search_results'),

]
