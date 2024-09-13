from django.contrib import admin

# Register your models here.
from .models import Job, Blog, ContactSubmission

class JobAdmin(admin.ModelAdmin):
    # Specify the list_display as a tuple. 
    list_display = ('title', 'company', 'location')
    
    # Add JobAdmin as an argument.
admin.site.register(Job, JobAdmin) # Register the Job model in Django admin, so you can manage the job listings here.

# Register Blog Model in Django Admin:
admin.site.register(Blog)

# Register the Contact Form submission Model in the Django Admin:
@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'submitted_at')
    list_filter = ('submitted_at',)