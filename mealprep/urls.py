from django.urls import path
from . import views

urlpatterns = [
    # public
    path("",              views.index,          name="index"),
    path("login/",        views.login_view,     name="login"),
    path("register/",     views.register_view,  name="register"),
    path("logout/",       views.logout_view,    name="logout"),

    # pages
    path("dashboard/",    views.dashboard,      name="dashboard"),
    path("favorites/",    views.favorites,      name="favorites"),
    path("grocery/",      views.grocery,        name="grocery"),
    path("calories/",     views.calories,       name="calories"),

    # recipe API
    path("api/recipes/",                         views.api_recipe_list,   name="api_recipe_list"),
    path("api/recipes/<int:recipe_id>/",         views.api_recipe_detail, name="api_recipe_detail"),
    path("api/recipes/<int:recipe_id>/toggle/",  views.api_toggle_star,   name="api_toggle_star"),
]
