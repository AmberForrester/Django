from django.contrib import admin

# Register your models here.
from .models import Job, Blog, ContactSubmission

# Register the Job model with additional admin options:
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'created_at', 'updated_at')
    search_fields = ('title', 'company', 'location')
    list_filter = ('created_at', 'location')
    readonly_fields = ('created_at', 'updated_at')  # Timestamps readonly in the admin panel
    
    # Add JobAdmin as an argument.
admin.site.register(Job, JobAdmin) # Register the Job model in Django admin, so you can manage the job listings here.


# Register the Blog model with additional admin options:
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'author__username')  # Search blogs by title and author's username
    list_filter = ('created_at', 'author')  # Add filter options by date and author
    readonly_fields = ('created_at',)  # Make created_at field readonly
    
# Register Blog Model in Django Admin:
admin.site.register(Blog, BlogAdmin)



# Register the ContactSubmission model with additional admin options:
@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'submitted_at')
    list_filter = ('submitted_at',)
    search_fields = ('name', 'email')  # Search contact submissions by name or email
    readonly_fields = ('submitted_at',)  # Make submitted_at field readonly