from django.shortcuts import render
from assignments.models import About
from blogs.models import Blog, Category


def home(request):
    featured_posts = Blog.objects.filter(is_featured=True).order_by('-updated_at')
    posts = Blog.objects.filter(is_featured=False, status="Published")

    #Fetch about us

    try:
        about= About.objects.get()
    except:
        about = None

    context = {
        'featured_posts': featured_posts,
        'posts': posts,
        'about':about,
    }
    return render(request, 'home.html', context)