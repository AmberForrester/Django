from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# Store Job Data in a Django Model: storing the job listings in a DB using Django's ORM. Then fetch and display the data in HTML template. 
# Create a Django Model to represent the job listings: 
class Job(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()
    apply_link = models.URLField()

    def __str__(self):
        return self.title
    
    
    
# Create a new Blog model to store blog posts: 
class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    


# Define a model for the contact form in models.py:
class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Message from {self.name} ({self.email})'