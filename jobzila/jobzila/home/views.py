from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Job, Blog
from .forms import BlogForm
from django.contrib.auth.decorators import login_required

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
    category = request.GET.get('category', '').strip()
    
    # Initialize an empty list for jobs:
    jobs = []
    
    # Check if a search query has been made( when keywords, location, or category is provided)
    search = any([keywords, location, category])
    
    if search:
        # Build the job filter based on the search query:
        jobs = Job.objects.all()
        
        # Filter by keywords in title or description, if provided
        if keywords:
            jobs = jobs.filter(title__icontains=keywords) | jobs.filter(description__icontains=keywords)
            
        # Filter by location, if provided
        if location:
            jobs = jobs.filter(location__icontains=location)

        # Filter by category, if provided
        if category:
            jobs = jobs.filter(category__icontains=category)

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

# View to add a new blog (for admin):
@login_required
def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('blog_list')
    
    else: 
        form = BlogForm()
    return render(request, 'home/add_blog.html', {'form': form})