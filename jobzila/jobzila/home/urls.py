from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'), # Map the URL http://127.0.0.1:8000/ to your homepage view. 
    # Now, include the URLs from the home app in the project-level urls.py located in jobzila/urls.py. 
    
    #2nd step - Create the URL route for the contact us page. So when users visit http://127.0.0.1:8000/contact/ they are directed to the contact us page.
    path('contact/', views.contact_us, name='contact_us'),
    
    # Define a URL route to serve the job listings page. 
    path('jobs/', views.job_listings, name='job_listings'),
    path('terms/', views.terms, name='terms'),
    path('privacy', views.privacy, name='privacy'),
]
