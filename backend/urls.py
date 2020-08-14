"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, re_path
from core import views, models

urlpatterns = [
    re_path(r'issues/(?P<id>\d+)|issues', views.resource(models.Issue)),
    re_path(r'contributors/(?P<id>\d+)|contributors', views.resource(models.Contributor)),
    re_path(r'organizations/(?P<id>\d+)|organizations', views.resource(models.Organization)),
    re_path(r'teams/(?P<id>\d+)|teams', views.resource(models.Team)),
    re_path(r'team_memberships/(?P<id>\d+)|team_memberships', views.resource(models.TeamMembership)),
    re_path(r'comments/(?P<id>\d+)|comments', views.resource(models.Comment)),    
]
