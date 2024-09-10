from django.contrib import admin

# Register your models here.
from .models import Job

class JobAdmin(admin.ModelAdmin):
    # Specify the list_display as a tuple. 
    list_display = ('title', 'company', 'location',)
    
    # Add JobAdmin as an argument.
admin.site.register(Job, JobAdmin) # Register the Job model in Django admin, so you can manage the job listings here. 