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
from django.urls import path
from core import views, models

urlpatterns = [
    path(r'issues.json/', views.read_many(models.Issue)),
    path(r'issues/<id>.json/', views.read_one(models.Issue)),
    path(r'contributors.json/', views.read_many(models.Contributor)),
    path(r'contributors/<id>.json/', views.read_one(models.Contributor)),
    path(r'organizations.json/', views.read_many(models.Organization)),
    path(r'organizations/<id>.json/', views.read_one(models.Organization)),
    path(r'teams.json/', views.read_many(models.Team)),
    path(r'teams/<id>.json/', views.read_one(models.Team)),
    path(r'teammemberships.json/', views.read_many(models.TeamMembership)),
    path(r'teammemberships/<id>.json/', views.read_one(models.TeamMembership)),
    path(r'comments.json/', views.read_many(models.Comment)),
    path(r'comments/<id>.json/', views.read_one(models.Comment)),
    path(r'test2/', views.test)
    #path(r'contributors/<id>', views.read_many(models.Contributor)),
]
