from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django import forms

class Contributor(AbstractBaseUser):
    username = models.CharField(max_length=15, unique=True)
    USERNAME_FIELD = "username"
    email = models.EmailField(max_length=300)
    bio = models.CharField(max_length=1000)
    

class Issue(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=10000)
    author = models.OneToOneField(
        Contributor,
        on_delete=models.CASCADE,
        primary_key=True,
    )

