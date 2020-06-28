from django.shortcuts import render
from . models import Comments, Post
from django.views.generic import ListView

# Create your views here.
def home(request):
    context = {
        'posts':Post.objects.all().order_by("-date_created")
    }
    return render (request, "blog/home.html", context)

def comments(request, post_id):
    return render(request, "blog/comments.html")