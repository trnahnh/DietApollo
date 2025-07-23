import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt

from .models import Recipe, GroceryItem, CalorieEntry
from .forms  import RecipeForm, GroceryForm, CalorieForm


# ------------------------------------------------------------------ #
#  FRONT-END PAGES
# ------------------------------------------------------------------ #
def index(request):
    return render(request, "mealprep/index.html")


def register_view(request):
    form = UserCreationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect("dashboard")
    return render(request, "mealprep/register.html", {"form": form})


def login_view(request):
    form = AuthenticationForm(data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        login(request, form.get_user())
        return redirect("dashboard")
    return render(request, "mealprep/login.html", {"form": form})


@login_required
def logout_view(request):
    logout(request)
    return redirect("index")


@login_required
def dashboard(request):
    return render(request, "mealprep/dashboard.html")


@login_required
def favorites(request):
    favs = Recipe.objects.filter(user=request.user, starred=True).order_by("-id")
    context = {"favorites": [_serialize(r) for r in favs]}
    return render(request, "mealprep/favorites.html", context)


@login_required
def grocery(request):
    items = GroceryItem.objects.filter(user=request.user).order_by("-id")
    form  = GroceryForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return redirect("grocery")
    return render(request, "mealprep/grocery.html", {"items": items, "form": form})


@login_required
def calories(request):
    entries = CalorieEntry.objects.filter(user=request.user).order_by("-created_at")
    form    = CalorieForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return redirect("calories")
    return render(request, "mealprep/calories.html", {"entries": entries, "form": form})


# ------------------------------------------------------------------ #
#  SERIALISER
# ------------------------------------------------------------------ #
def _serialize(recipe: Recipe) -> dict:
    return {
        "id":          recipe.id,
        "title":       recipe.title,
        "ingredients": [s.strip() for s in recipe.ingredients.split(",") if s.strip()],
        "instructions": [s.strip() for s in recipe.instructions.split(",") if s.strip()],
        "starred":     recipe.starred,
    }


# ------------------------------------------------------------------ #
#  RECIPE LIST  (GET / POST)
# ------------------------------------------------------------------ #
@csrf_exempt
@login_required
def api_recipe_list(request):
    user = request.user

    if request.method == "GET":
        qs = Recipe.objects.filter(user=user).order_by("-id")
        return JsonResponse([_serialize(r) for r in qs], safe=False)

    if request.method == "POST":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return HttpResponseBadRequest("Bad JSON")

        form = RecipeForm(data)
        if not form.is_valid():
            return JsonResponse({"errors": form.errors}, status=400)

        new = form.save(commit=False)
        new.user = user
        new.save()
        return JsonResponse(_serialize(new), status=201)

    return HttpResponseNotAllowed(["GET", "POST"])


# ------------------------------------------------------------------ #
#  RECIPE DETAIL  (GET / PUT / DELETE)
# ------------------------------------------------------------------ #
@csrf_exempt
@login_required
def api_recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id, user=request.user)

    if request.method == "GET":
        return JsonResponse(_serialize(recipe))

    if request.method == "PUT":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return HttpResponseBadRequest("Bad JSON")

        form = RecipeForm(data, instance=recipe)
        if not form.is_valid():
            return JsonResponse({"errors": form.errors}, status=400)

        form.save()
        return JsonResponse(_serialize(recipe))

    if request.method == "DELETE":
        recipe.delete()
        return JsonResponse({"deleted": True})

    return HttpResponseNotAllowed(["GET", "PUT", "DELETE"])


# ------------------------------------------------------------------ #
#  TOGGLE STAR
# ------------------------------------------------------------------ #
@csrf_exempt
@login_required
def api_toggle_star(request, recipe_id):
    if request.method != "PUT":
        return HttpResponseNotAllowed(["PUT"])

    recipe = get_object_or_404(Recipe, id=recipe_id, user=request.user)
    recipe.starred = not recipe.starred
    recipe.save()
    return JsonResponse({"starred": recipe.starred})
