from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . models import Comments, Post
from django.views.generic import ListView

# Create your views here.
#def error_404_view(request, exception):
#    return render(request,'blog/error.html')

def home(request):
    context = {
        'posts':Post.objects.all().order_by("-date_created")
    }
    return render (request, "blog/home.html", context)

def comments(request, post_id):
    
    context = {
        'comments':Comments.objects.filter(post_connection=post_id).order_by('-date_created'),
        'post':Post.objects.get(pk=post_id)
    }
    return render(request, "blog/comments.html", context)   
    
    