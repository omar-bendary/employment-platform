from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django_boost.models.fields import AutoOneToOneField


class Job(models.Model):
    LEVELS = (
        ("JR", "Junior"),
        ("MID", "Mid-Level"),
        ("SR", "Senior"),
    )
    title = models.CharField(max_length=50)
    published_at = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=50)
    experience_level = models.CharField(
        choices=LEVELS,
        max_length=3,
        default="JR",
    )
    description = models.TextField()
    employee = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="job"
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("job_list")


class Application(models.Model):
    brief = models.TextField(max_length=500)
    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        related_name="applications",
    )
    employee = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="applications",
    )

    def __str__(self):
        return self.job.title

    def get_absolute_url(self):
        return reverse("job_detail", args=[str(self.job.id)])


class EmploymentProcess(models.Model):
    STATUS = (
        ("APPLIED", "Applied"),
        ("APROVED", "Aproved"),
        ("REJECTED", "Rejected"),
    )
    application = AutoOneToOneField(
        Application,
        primary_key=True,
        related_name="employment_process",
        on_delete=models.CASCADE,
    )
    status = models.CharField(choices=STATUS, default="APPLIED", max_length=10)

    def __str__(self):
        return self.status
