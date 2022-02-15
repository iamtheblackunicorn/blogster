# BLOGSTER by Alexander Abraham
# a.k.a. "The Black Unicorn" a.k.a. "Angeldust Duke".
# Licensed under the MIT license.

from .models import Post
from django.shortcuts import render
from django.http import JsonResponse

def blog(request):
    all_posts = Post.objects.all()
    return render(
        request,
        'posts/blog.html',
        {
            'posts':all_posts
        }
    )

def post(request, title):
    post = Post.objects.get(title=title)
    post_body = post.body
    post_date = post.date
    post_description = post.description
    return render(
        request,
        'posts/post.html',
        {
            'title':title,
            'body':post_body,
            'date':post_date,
            'description':post_description
        }
    )
