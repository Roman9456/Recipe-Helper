from django.shortcuts import render
from django.http import HttpResponseBadRequest


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
 
}

def calculate_recipe(request, recipe_name):

    servings = int(request.GET.get('servings', 1))

 
    recipe = DATA.get(recipe_name)
    if not recipe:
        return HttpResponseBadRequest('Рецепт не найден.')

    
    scaled_recipe = {ingredient: amount * servings for ingredient, amount in recipe.items()}

    
    context = {
        'recipe': scaled_recipe,
    }

    return render(request, 'calculator/index.html', context)
