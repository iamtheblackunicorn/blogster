# BLOGSTER by Alexander Abraham
# a.k.a. "The Black Unicorn" a.k.a. "Angeldust Duke".
# Licensed under the MIT license.

from . import views
from django.urls import path
app_name = 'posts'
urlpatterns = [
    path('', views.blog, name='blog'),
    path('api', views.api, name='api'),
    path('<str:title>', views.post, name='post'),
]
