from django.contrib import admin
from jobs.models import Job, Application, EmploymentProcess

admin.site.register(Job)
admin.site.register(Application)
admin.site.register(EmploymentProcess)
