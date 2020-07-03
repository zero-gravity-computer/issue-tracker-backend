from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser 

class Author(AbstractBaseUser):
    username = models.CharField(max_length=15, unique=True)
    USERNAME_FIELD = "username"
    bio = models.CharField(max_length=500)
    

class Issue(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    author = models.OneToOneField(
        Author,
        on_delete=models.CASCADE,
        primary_key=True,
    )
