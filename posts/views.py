# BLOGSTER by Alexander Abraham
# a.k.a. "The Black Unicorn" a.k.a. "Angeldust Duke".
# Licensed under the MIT license.

from .models import Post
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse

def blog(request):
    """
    Fetches all post objects
    and returns the [posts/blog.html]
    template with an iterator for context.
    """
    all_posts = Post.objects.all()
    context = {
        'posts':all_posts
    }
    context.update(settings.SITE_VARS)
    return render(
        request,
        'posts/blog.html',
        context
    )

def post(request, title):
    """
    Fetches a post object by title
    and returns the [posts/post.html]
    template with all post data for context.
    """
    post = Post.objects.get(title=title)
    post_body = post.body
    post_date = post.date
    post_description = post.description
    context = {
        'title':title,
        'body':post_body,
        'date':post_date,
        'description':post_description
    }
    context.update(settings.SITE_VARS)
    return render(
        request,
        'posts/post.html',
        context
    )

def settings_api(request):
    """
    We return a [JsonResponse]
    of global site variables, if desired.
    """
    return JsonResponse(settings.SITE_VARS, safe=False)

def api(request):
    """
    Fetches all post objects,
    serializes them in a dictinary,
    and returns a [JsonResponse].
    """
    all_posts = Post.objects.all()
    result = {}
    for post in all_posts:
        body = post.body
        date = post.date
        title = post.title
        description = post.description
        result[title] = [
            description,
            body,
            date
        ]
    return JsonResponse(result, safe=False)
