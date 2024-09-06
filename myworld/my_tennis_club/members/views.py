# Create your views here.

from django.http import HttpResponse
from django.template import loader
from .models import Member # Import the Member model

def members(request):
    mymembers = Member.objects.all().values() # Creates a mymembers object with all the values of the Member model
    
    template = loader.get_template('all_members.html') # Loads the all_members.html template
    
    context = {
        'mymembers': mymembers, # Creates an object containing the mymembers object
    }
    return HttpResponse(template.render(context, request)) # Sends the object to the template, outputs the HTML that is rendered by the template. 

