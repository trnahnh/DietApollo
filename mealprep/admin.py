from django.contrib import admin
from .models import User, Recipe, GroceryItem, Favorite, CalorieEntry

admin.site.register(User)
admin.site.register(Recipe)
admin.site.register(GroceryItem)
admin.site.register(Favorite)
admin.site.register(CalorieEntry)
