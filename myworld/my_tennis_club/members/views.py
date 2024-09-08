# Create your views here.

from django.http import HttpResponse
from django.template import loader
from .models import Member # Import the Member model

# View custom 404 page during development (with DEBUG=True), needing to manually raise a 404 error (Http404 exception) in a view.
# Manually testing the 404 page, by simulating a 404 error in one of your views to test the custom 404 error page. 
from django.http import Http404
from django.shortcuts import render

def test_404_view(request):
    raise Http404('Sorry, this page does not exist.')


# The Tennis Club Members List view - 
def members(request):
    mymembers = Member.objects.all().values() # Creates a mymembers object with all the values of the Member model.
    
    template = loader.get_template('all_members.html') # Loads the all_members.html template.
    
    context = {
        'mymembers': mymembers, # Creates an object containing the mymembers object.
    }
    return HttpResponse(template.render(context, request)) # Sends the object to the template, outputs the HTML that is rendered by the template. 



# New View created to deal with incoming requests to the /details/ url.
# The details view - 
def details(request, id): # Get an id as an argument.
    mymember = Member.objects.get(id=id) # Uses the id to locate correct record in the Member table.
    
    template = loader.get_template('details.html') # Loads the details template.
    context = {
        'mymember': mymember, # Creates an object containing the member.
    }
    return HttpResponse(template.render(context, request)) # Sends the object to the template, outputs the HTML that is rendered by the template. 



# Home, landing page View - 
def main(request):
    template = loader.get_template('main.html') # Load the main.html template.
    return HttpResponse(template.render()) # Outputs the HTML rendered by template.



# Add a Testing View -
def testing(request):
    template = loader.get_template('template.html')
    context = {
        'teamname': ['Elites', 'Newbies', 'Warriors'],
    }
    return HttpResponse(template.render(context, request))