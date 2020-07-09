from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django import forms

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Contributor(TimeStampedModel, AbstractBaseUser):
    username = models.CharField(max_length=15, unique=True)
    USERNAME_FIELD = "username"
    email = models.EmailField(max_length=300)
    bio = models.CharField(max_length=1000)
    


class Organization(models.Model):
    name = models.CharField(max_length=80, unique=True)

class Team(TimeStampedModel):
    name = models.CharField(max_length=80)
    contributor = models.ManyToManyField(
        Contributor,
    )
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE
    )

    
class TeamMembership(TimeStampedModel):
    contributor = models.ForeignKey(
        Contributor,
        on_delete=models.CASCADE
    )
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE
    )

class Issue(TimeStampedModel):
   
    class Severity(models.TextChoices):
        low = 'Low'
        medium = 'Medium'
        high = 'High'

    severity = models.CharField(
        max_length=32,
        choices=Severity.choices,
        default=Severity.medium,
    )
        
    class Status(models.TextChoices):
        not_started = 'Not Started'
        in_progress = 'In Progress'
        completed = 'Completed'
        
    status = models.CharField(
        max_length=32,
        choices=Status.choices,
        default=Status.not_started,
        )
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=2048)
    author = models.ForeignKey(
        Contributor,
        on_delete=models.SET_NULL,
        null=True
    )
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
    )
class Comment(TimeStampedModel):
    body = models.CharField(max_length=2048)
    author = models.ForeignKey(
        Contributor,
        on_delete=models.SET_NULL,
        null=True,
    )
    issue = models.ForeignKey(
        Issue,
        on_delete=models.CASCADE,
    ) 