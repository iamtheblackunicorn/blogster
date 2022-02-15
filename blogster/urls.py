# BLOGSTER by Alexander Abraham
# a.k.a. "The Black Unicorn" a.k.a. "Angeldust Duke".
# Licensed under the MIT license.

from django.urls import path
from django.urls import include
from django.contrib import admin
urlpatterns = [
    path('god', admin.site.urls),
    path('', include('posts.urls'))
]
