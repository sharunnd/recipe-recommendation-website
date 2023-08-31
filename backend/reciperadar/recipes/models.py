from django.db import models

# Create your models here.
# recipes/models.py
# recipes/models.py
from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    heading = models.CharField(max_length=255)
    ingredients = models.TextField()

    def __str__(self):
        return self.heading
