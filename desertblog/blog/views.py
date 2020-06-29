from django.shortcuts import render, redirect
from .models import Comments, Post


def home(request):
    context = {
        'posts':Post.objects.all().order_by("-date_created")
    }
    return render (request, "blog/home.html", context)


def comments(request, post_id):
    
    if not Post.objects.get(pk=post_id):
        return render (request, "blog/error.html")

    comment = Comments.objects.filter(post_connection=post_id).order_by('-date_created')
    context = {
        'comments': comment,
        'post':Post.objects.get(pk=post_id)
    }
    
    return render(request, "blog/comments.html", context)   

def add_comment(request, post_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect ('home')
    else:
        form = CommentForm()

    return render(request, "blog/add_comment.html", {"form":form}) 

    