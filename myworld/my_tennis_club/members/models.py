# Create your models here (actually tables in a DB)

from django.db import models

class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)
    
# To change the display of Members Model in the Admin User Interface.
# You can change the string representation, by defining the __str__() function of the Member Model.
# at the end of the about data fields, add the following code block:
# def __str__(self):
#   return f'{self.firstname} {self.lastname}'
# This is will diplay Member by first and last name. 

# Defining a __str__() function is NOT a Django feature, it is how to change the string representation of objects in Python. 