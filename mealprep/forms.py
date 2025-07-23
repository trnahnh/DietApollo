from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, Recipe, GroceryItem, CalorieEntry

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

class LoginForm(AuthenticationForm):
    pass

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ["title", "ingredients", "instructions"]

class GroceryForm(forms.ModelForm):
    class Meta:
        model = GroceryItem
        fields = ["name", "notes"]

class CalorieForm(forms.ModelForm):
    class Meta:
        model = CalorieEntry
        fields = ["protein", "carbs", "calories"]
