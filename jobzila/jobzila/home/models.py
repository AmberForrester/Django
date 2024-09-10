from django.db import models

# Create your models here.


# Store Job Data in a Django Model: storing the job listings in a DB using Django's ORM. Then fetch and display the data in HTML template. 
# Create a Django Model to represent the job listings. 
class Job(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()
    apply_link = models.URLField()

    def __str__(self):
        return self.title