from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django import forms

class Contributor(AbstractBaseUser):
    username = models.CharField(max_length=15, unique=True)
    USERNAME_FIELD = "username"
    email = models.EmailField(max_length=300)
    bio = models.CharField(max_length=1000)

class Status(models.Model):
    Not_Started = 0
    In_Progress = 1
    Completed = 2
    Status_Choices = [
        (Not_Started, 'Not Started'),
        (In_Progress, 'In Progress'),
        (Completed, 'Completed'),
    ]
    status_choices = models.IntegerField(
        choices=Status_Choices,
        default=Not_Started
    )
class Severity(models.Model):
    Low = 0
    Medium = 1
    High = 2
    Severity_Choices = [
        (Low, 'Low'),
        (Medium, 'Medium'),
        (High, 'High'),
    ]
    Severity_choices = models.IntegerField(
        choices=Severity_Choices,
        default=Medium
    )
class Group(models.Model):
    name = models.CharField(max_length=150)

class GroupMembership(models.Model):
    contributor = models.ForeignKey(
        Contributor,
        on_delete=models.CASCADE
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE
    )
    is_owner = models.BooleanField()

class Issue(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=2048)
    author = models.OneToOneField(
        Contributor,
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

