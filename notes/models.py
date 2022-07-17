from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#every time you make a model make sure you makemigrations then migrate
#if you want to look at db go to the shell
class Note(models.Model):
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)#connects note to user

    
    def __str__(self):  #necessary to show actual text in DB instead of "object"
        return self.body
    