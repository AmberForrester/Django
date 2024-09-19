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
    
    # ADMIN only views for Jobs
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('view-contact-form', views.view_contact_form, name='view_contact_form'),
    path('manage-jobs/', views.manage_jobs, name='manage_jobs'),
    path('jobs/add/', views.add_job, name='add_job'),
    path('jobs/edit/<int:job_id>/', views.edit_job, name='edit_job'),
    path('jobs/delete/<int:job_id>/', views.delete_job, name='delete_job'),
    
    # ADMIN only views for Blogs
    path('manage-blogs/', views.manage_blogs, name='manage_blogs'),
    path('blogs/add/', views.add_blog, name='add_blog'),
    path('blogs/edit/<int:blog_id>/', views.edit_blog, name='edit_blog'),
    path('blogs/delete/<int:blog_id>/', views.delete_blog, name='delete_blog'),
    
    # Authentication URLs
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(next_page='homepage'), name='logout'),
    path('login/success/', views.login_sucess, name='login_success'),
]
    
    