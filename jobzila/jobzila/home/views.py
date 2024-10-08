from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Job, Blog, ContactSubmission
from .forms import BlogForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages



# Created a simple function that returns a homepage response:
def homepage(request):
    return render(request, 'home/index.html')

# This tells Django to look for an index.html template inside a home/templates/home/ folder. 

# 1st step - create a view for the Contact Us Page that will render the HTML template.
def contact_us(request):
    
    # Handling form submission - if you want to process the form (ex. send an email or save the data), youll need to update the function here. 
    # Get form data from the POST request:
    if request.method == 'POST':
        # Here you can process the form (e.g., save the data or send an email)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Save the form data to the database
        contact_submission = ContactSubmission(name=name, email=email, message=message)
        contact_submission.save()  # Make sure the form is actually being saved
        
        # Send an email to the Admin:
        send_mail(
            subject=f'New Contact Form Submission From {name}',
            message=f'You have received a new message from {name} ({email}).\n\nMessage:\n{message}',
            from_email=settings.DEFAULT_FROM_EMAIL, # From Email (must be set in settings.py)
            recipient_list=[settings.ADMIN_EMAIL], # Admin email address
            fail_silently=False,
        )
        
        # Show a success message to the user:
        messages.success(request, 'Thank you for your message. We will get back to you within 24 hours. Have a great day, we look forward to speaking with you.')
        
        # Return to a Thank-You page or back to the form: 
        return redirect('contact_us')
    
    # If the request is GET, just display the contact form:
    return render(request, 'home/contactus.html')



# Create a view that fetches the job listigs from the DB and passes them to a template:
def job_listings(request):
    jobs = Job.objects.all() # Fetch all jobs from the DB.
    return render(request, 'home/joblistings.html', {'jobs': jobs})

def terms(request):
    return render(request, 'home/terms.html')

def privacy(request):
    return render(request, 'home/privacy.html')

# Create a view function to render job searches.
# Jobs are filtered based on the provided keyword and location. 
def job_search(request):
    
    # Get the search parameters for keywords, location, and category:
    keywords = request.GET.get('keywords', '').strip()
    location = request.GET.get('location', '').strip()
    category = request.GET.get('category', '').strip()  # Now treated as a keyword for title and description search
    
    # Initialize an empty list for jobs:
    jobs = Job.objects.all()
    
    # Check if a search query has been made( when keywords, location, or category is provided)
    search = any([keywords, location, category])
    
    if search:
        # Filter by keywords in title or description, if provided
        if keywords:
            jobs = jobs.filter(Q(title__icontains=keywords) | Q(description__icontains=keywords))
        
        # Filter by location, if provided
        if location:
            jobs = jobs.filter(location__icontains=location)

        # Treat the selected category as an additional keyword to search in both title and description
        if category:
            jobs = jobs.filter(Q(title__icontains=category) | Q(description__icontains=category))

     # Render the jobsearch.html template and pass the jobs and search parameters
    return render(request, 'home/jobsearch.html', {
        'jobs': jobs,
        'keywords': keywords,
        'location': location,
        'category': category,
        'search': search  # Pass this to the template to control result display
    })
    
    
    
# View to display a list of all blogs:
def blog_list(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'home/blog_list.html', {'blogs': blogs})

# View to display a specific blog post by its ID:
def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'home/blog_detail.html', {'blog': blog})    
    


# Custom decorator to check if user is an admin only:
def admin_required(function=None):
    actual_decorator = user_passes_test(lambda u: u.is_superuser)
    if function:
        return actual_decorator(function)
    return actual_decorator

# Custom Admin Dashboard View:
# Only logged-in superusers(admins) can access the Admin Dashboard
@login_required
@user_passes_test(admin_required)
def admin_dashboard(request):
    return render(request, 'home/admin_dashboard.html') 

# Redirect admins to the dashboard upon login:
def login_success(request):
    if request.user.is_superuser: # If the user is an Admin
        return redirect('admin_dashboard')
    else:
        return redirect('job_listings') # Regular users go to homepage


 
# MANAGE JOBS - only for admin: 
@login_required
@admin_required
def manage_jobs(request):
    jobs = Job.objects.all()
    return render(request, 'home/manage_jobs.html', {'jobs': jobs})

# Add Jobs - only for admin:
@login_required
@admin_required
def add_job(request):
    if request.method == 'POST':
        title = request.POST['title']
        company = request.POST['company']
        location = request.POST['location']
        description = request.POST['description']
        apply_link = request.POST['apply_link']

        job = Job(title=title, company=company, location=location, description=description, apply_link=apply_link)
        job.save()
        return redirect('manage_jobs')

    return render(request, 'home/add_job.html') 

# Edit Jobs - only for admin:
@login_required
@admin_required
def edit_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    if request.method == 'POST':
        job.title = request.POST['title']
        job.company = request.POST['company']
        job.location = request.POST['location']
        job.description = request.POST['description']
        job.apply_link = request.POST['apply_link']
        job.save()
        return redirect('manage_jobs')
    
    return render(request, 'home/edit_job.html', {'job': job})

# Delete Jobs - only for admin:
@login_required
@admin_required
def delete_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    job.delete()
    return redirect('manage_jobs')



# MANAGE BLOGS - only for admin:
@login_required
@admin_required
def manage_blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'home/manage_blogs.html', {'blogs': blogs})

# Add blogs - only for admin:
@login_required
@admin_required
def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('manage_blogs')

    form = BlogForm()
    return render(request, 'home/add_blog.html', {'form': form})

# Edit blogs - only for admin: 
def edit_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == 'POST':
        blog.title = request.POST['title']
        blog.content = request.POST['content']
        blog.save()
        return redirect('manage_blogs')
    
    return render(request, 'home/edit_blog.html', {'blog': blog})

# Delete blogs - only for admin:
@login_required
@admin_required
def delete_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    blog.delete()
    return redirect('manage_blogs')

# View contact form submissions:
@login_required
@admin_required
def view_contact_form(request):
    contact_forms = ContactSubmission.objects.all() # Fetch all contact form submissions from the DB
    return render(request, 'home/view_contact_form.html',{'contact_forms': contact_forms})