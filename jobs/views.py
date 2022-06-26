from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Job, Application
from django.db.models import Q


class JobListView(ListView):
    model = Job
    template_name = "jobs/home.html"
    context_object_name = "job_list"
    paginate_by = 5

    # sort jobs by newest
    def get_queryset(self, *args, **kwargs):
        qs = super(JobListView, self).get_queryset(*args, **kwargs)
        qs = qs.order_by("-published_at")
        return qs


class JobDetailView(LoginRequiredMixin, DetailView):
    model = Job
    template_name = "jobs/job_detail.html"


class JobCreateView(LoginRequiredMixin, CreateView):
    model = Job
    template_name = "jobs/new_job.html"
    fields = ["title", "location", "experience_level", "description"]

    def form_valid(self, form):
        form.instance.employee = self.request.user
        return super().form_valid(form)


class ApplyView(LoginRequiredMixin, CreateView):
    model = Application
    template_name = "jobs/job_apply.html"
    fields = [
        "brief",
    ]

    # Prefill user and job when apply to a job
    def form_valid(self, form,):
        form.instance.employee = self.request.user
        pk = self.kwargs.get(self.pk_url_kwarg)
        job = Job.objects.get(pk=pk)
        form.instance.job = job

        return super().form_valid(form)


class SearchResultsListView(ListView):
    model = Job
    context_object_name = 'job_search_list'
    template_name = 'jobs/search_results.html'
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Job.objects.filter(
            Q(title__icontains=query) | Q(location__icontains=query) | Q(
                experience_level__icontains=query) | Q(description__icontains=query)

        )
