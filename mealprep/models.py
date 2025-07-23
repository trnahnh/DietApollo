from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    ingredients = models.TextField()
    instructions = models.TextField()
    starred = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "ingredients": self.ingredients,
            "instructions": self.instructions,
            "starred": self.starred,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        }

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

class GroceryItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    notes = models.TextField(blank=True)

class CalorieEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    protein = models.FloatField()
    carbs = models.FloatField()
    calories = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def serialize(self):
        return {
            "id": self.id,
            "protein": self.protein,
            "carbs": self.carbs,
            "calories": self.calories,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        }
