from django.shortcuts import render
from django.http import HttpResponse
from .models import Job

# Create your views here.


# Created a simple function that returns a homepage response:
def homepage(request):
    return render(request, 'home/index.html')

# This tells Django to look for an index.html template inside a home/templates/home/ folder. 

# 1st step - create a view for the Contact Us Page that will render the HTML template.
def contact_us(request):
    
    # Handling form submission - if you want to process the form (ex. send an email or save the data), youll need to update the function here. 
    # For now let us diplay a success message when the form is submitted: 
    if request.method == 'POST':
        # Here you can process the form (e.g., save the data or send an email)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Return simple success message:
        return HttpResponse(f'Thanks for reaching out, {name}! We will get back to you within 24 hours.')
    
    return render(request, 'home/contactus.html')

# Create a view that fetches the job listigs from the DB and passes them to a template:
def job_listings(request):
    jobs = Job.objects.all() # Fetch all jobs from the DB
    return render(request, 'home/joblistings.html', {'jobs': jobs})
