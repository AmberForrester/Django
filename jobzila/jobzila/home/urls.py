from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.homepage, name='homepage'), # Map the URL http://127.0.0.1:8000/ to your homepage view. 
    # Now, include the URLs from the home app in the project-level urls.py located in jobzila/urls.py. 
    
    #2nd step - Create the URL route for the contact us page. So when users visit http://127.0.0.1:8000/contact/ they are directed to the contact us page.
    path('contact/', views.contact_us, name='contact_us'),
    
    # Define a URL route to serve the job listings page. 
    path('jobs/', views.job_listings, name='job_listings'),
    path('terms/', views.terms, name='terms'),
    path('privacy', views.privacy, name='privacy'),
    path('jobsearch', views.job_search, name='job_search'),
    path('blogs/', views.blog_list, name='blog_list'),
    path('blogs/<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('blogs/add/', views.add_blog, name='add_blog'),
    path('accounts/login/', LoginView.as_view(), name='login'), # Map the /accounts/login/ URL to Django's built-in LoginView. 
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
]
    
    