from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django import forms

class Contributor(AbstractBaseUser):
    username = models.CharField(max_length=15, unique=True)
    USERNAME_FIELD = "username"
    email = models.EmailField(max_length=300)
    bio = models.CharField(max_length=1000)

class Status(models.Model):
    not_started = 0
    in_progress = 1
    completed = 2
    status_choices = [
        (not_started, 'Not Started'),
        (in_progress, 'In Progress'),
        (completed, 'Completed'),
    ]
    status = models.IntegerField(
        choices=status_choices,
        default=not_started
    )
class Severity(models.Model):
    low = 0
    medium = 1
    high = 2
    severity_choices = [
        (low, 'Low'),
        (medium, 'Medium'),
        (high, 'High'),
    ]
    severity = models.IntegerField(
        choices=severity_choices,
        default=medium
    )
  class Organization(models.Model):
    name = models.CharField(max_length=150)
 
class Team(models.Model):
    name = models.CharField(max_length=80)
    contributor = models.ManyToManyField(
        Contributor,
    )
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE
    )
    is_owner = models.BooleanField()
    
class TeamMembership(models.Model):
    contributor = models.ForeignKey(
        Contributor,
        on_delete=models.CASCADE
    )
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE
    )

class Issue(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=2048)
    author = models.OneToOneField(
        Contributor,
        on_delete=models.SET_NULL,
        null=True
    )
    organization = models.OneToOneField(
        Organization,
        on_delete=models.CASCADE,
    )
    team = models.OneToOneField(
        Team,
        on_delete=models.SET_NULL,
        null=True
    )
class Comment(models.Model):
    body = models.CharField(max_length=2048)
    author = models.OneToOneField(
        Contributor,
        on_delete=models.SET_NULL,
        null=True,
    )
    issue = models.OneToOneField(
        Issue,
        on_delete=models.CASCADE,
    ) 

