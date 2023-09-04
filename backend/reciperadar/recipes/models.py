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
    image_url = models.URLField(blank=True, null=True)
    average_rating = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    num_reviews = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.heading


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=3, decimal_places=1)  # You can choose an appropriate field type for ratings

    def __str__(self):
        return f"{self.user.username}'s rating for {self.recipe.heading}"

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    comment = models.TextField()
    user_name = models.CharField(max_length=255)  # Add this field for the user's name

    def save(self, *args, **kwargs):
        if not self.user_name:
            self.user_name = self.user.username  # Set user_name to the username if not provided
        super().save(*args, **kwargs)
        # Increment the num_reviews field of the associated recipe
        self.recipe.num_reviews += 1
        self.recipe.save()



