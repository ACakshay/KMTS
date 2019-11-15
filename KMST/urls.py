"""KMST URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from kms import views
from django.views.generic import TemplateView
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from kms import views as core_views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^Team/$', TemplateView.as_view(template_name='ex1.html'), name='session'),
    url(r'^visual/$', TemplateView.as_view(template_name='about.html'), name='view_profile'),
    url(r'^show$', views.show, name='showres'),
    #url(r'^result$', views.view_profile, name='result'),

]
