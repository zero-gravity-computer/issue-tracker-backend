from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django import forms
from argon2 import PasswordHasher
from django_instant_rest.models import RestResource

ph = PasswordHasher()

class Contributor(RestResource):
    username = models.CharField(max_length=15, unique=True)
    USERNAME_FIELD = "username"
    password = models.CharField(max_length=200)
    email = models.EmailField(max_length=300)
    bio = models.CharField(max_length=1000)

    def save(self, *args, **kwargs):
        self.password = ph.hash(self.password)
        super(Contributor, self).save(*args, **kwargs)

    def verify_password(self, password):
        return ph.verify(self.password, password)


class Organization(RestResource):
    name = models.CharField(max_length=80, unique=True)

class Team(RestResource):
    name = models.CharField(max_length=80)
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE
    )

    
class TeamMembership(RestResource):
    contributor = models.ForeignKey(
        Contributor,
        on_delete=models.CASCADE
    )
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE
    )

class Issue(RestResource):
   
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
class Comment(RestResource):
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