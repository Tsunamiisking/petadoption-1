from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime


class User(AbstractUser):
    pass

class Category(models.Model):
    category = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.category}"




class Pet(models.Model):
    user = models.CharField(max_length=200, default="Admin")
    petname = models.CharField(max_length=200)
    breed = models.CharField(max_length=200)
    url = models.URLField(max_length=500)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    pet_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.petname}: {self.pet_category}"

class CommentNew(models.Model):
    user = models.CharField(max_length=200)
    comment_text = models.CharField(max_length=500)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now)

    def __str__(self):
        return f"{self.user}: {self.comment_text}"

class Featured_Pet(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pet}"



