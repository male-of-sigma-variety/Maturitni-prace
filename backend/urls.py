"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.etree.ElementInclude import include
from django import urls
from django.contrib import admin
from django.urls import path, include
from reviews.views import food_list_view, review_view, home_view
from register.views import register_view, invalid_form_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('jidla/', food_list_view, name='food_list'),
    path('jidla/<int:food_id>', review_view, name='food_reviews'),
    path('registrace/', register_view, name="register"),
    path('ohno/', invalid_form_view, name='invalid form'),
    path('', include("django.contrib.auth.urls")),
]
