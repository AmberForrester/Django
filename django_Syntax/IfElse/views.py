from django.http import HttpResponse
from django.template import loader

# Django If statement -
def testing(request):
  template = loader.get_template('template.html')
  context = {
    'greeting': 1,
  }
  return HttpResponse(template.render(context, request))  



# Elif keyword - 
def testing(request):
  template = loader.get_template('template.html')
  context = {
    'greeting': 2,
  }
  return HttpResponse(template.render(context, request)) 



# Else keyword -
def testing(request):
  template = loader.get_template('template.html')
  context = {
    'greeting': 3,
  }
  return HttpResponse(template.render(context, request)) 