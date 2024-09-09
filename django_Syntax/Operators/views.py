# View in browser: 127.0.0.1:8000/testing

from django.http import HttpResponse
from django.template import loader

# == equal to 
def testing(request):
  template = loader.get_template('template.html')
  context = {
    'greeting': 2,
  }
  return HttpResponse(template.render(context, request)) 



# != is not equal to 
def testing(request):
  template = loader.get_template('template.html')
  context = {
    'greeting': 2,
  }
  return HttpResponse(template.render(context, request))      



# < less than
def testing(request):
  template = loader.get_template('template.html')
  context = {
    'greeting': 2,
  }
  return HttpResponse(template.render(context, request))   



# <= is less than, or equal to
def testing(request):
  template = loader.get_template('template.html')
  context = {
    'greeting': 2,
  }
  return HttpResponse(template.render(context, request)) 



# > greater than
def testing(request):
  template = loader.get_template('template.html')
  context = {
    'greeting': 2,
  }
  return HttpResponse(template.render(context, request))  



# >= is greater than, or equal to
def testing(request):
  template = loader.get_template('template.html')
  context = {
    'greeting': 2,
  }
  return HttpResponse(template.render(context, request))   



# and - to check if more than one condition is true 
def testing(request):
  template = loader.get_template('template.html')
  context = {
    'greeting': 1,
    'day': 'Friday',    
  }
  return HttpResponse(template.render(context, request))   



# or - checks if one condition is true 
def testing(request):
  template = loader.get_template('template.html')
  context = {
    'greeting': 1,
  }
  return HttpResponse(template.render(context, request)) 



# Combine and/or
def testing(request):
  template = loader.get_template('template.html')
  context = {
    'greeting': 5,
    'day': 'Friday',    
  }
  return HttpResponse(template.render(context, request))           



# in - check if certain item is present in an object
def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request))    



# is - checks if TWO OBJECTS are the SAME
# checking the identity of two objects
# In the view we have two objects, x and y with the same values
def testing(request):
  template = loader.get_template('template.html')
  context = {
    'x': ['Apple', 'Banana', 'Cherry'],   
    'y': ['Apple', 'Banana', 'Cherry'],
  }
  return HttpResponse(template.render(context, request)) 

# within the template.html - The two objects have the same value BUT IT IS NOT THE SAME OBJECT x,y -> Having a NO result. 
# {% if x is y %}
# <h1>YES</h1>
#{% else %}
# <h1>NO</h1>
# {% endif %}

# How can two objects be the same? 
# If you have two objects that points to the same object, then the is operator evaluates to true.
# By using the {% with %} tag, which allows us to create variables in the template --> {% with var1=x var2=x %} -> Having a YES result. 
            #{% if var1 is var2 %}
            #<h1>YES</h1>
            #{% else %}
            #<h1>NO</h1>
            #{% endif %}
            #{% endwith %}
def testing(request):
  template = loader.get_template('template.html')
  context = {
    'x': ['Apple', 'Banana', 'Cherry'],   
    'y': ['Apple', 'Banana', 'Cherry'],
  }
  return HttpResponse(template.render(context, request)) 