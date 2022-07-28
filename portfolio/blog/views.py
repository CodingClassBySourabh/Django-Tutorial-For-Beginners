from django.http import HttpResponse
from django.shortcuts import render
from .models import Blog

# Create your views here.
def home(request):
    return render(request, "index.html")
    
def about(request):
    return render(request, "about.html")

def resume(request):
    return render(request, "resume.html")

def blog(request):
    blog = Blog.objects.all()
    context = {
        'blog': blog
    }
    return render(request, "blog.html", context)

def portfolio(request):
    return render(request, "portfolio.html")

def contact(request):
    return render(request, "contact.html")