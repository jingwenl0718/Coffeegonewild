from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.user_model import User
from flask_app.models.recipe_model import Recipe

# READ ALL ROUTE
@app.route("/coffeegonewild/all_recipes")
def all_recipes():
    all_recipes = Recipe.get_all()
    return render_template("recipes_all.html", all_recipes = all_recipes)

# READ ONE
@app.route("/coffeegonewild/viewrecipe/<int:id>")
def view_recipe(id):
    data = {
        'id': id
    }
    session['recipe_id'] = id
    recipe = Recipe.get_one(data)
    average_count = Recipe.calculate_avg_count(data)
    if average_count:
        avg_rating = average_count[0].get('avg_rating', 0)
        review_count = average_count[0].get('review_count', 0)
    else:
        avg_rating, review_count = 0, 0 
    return render_template("recipe_one.html", recipe = recipe, avg_rating=avg_rating, review_count=review_count)

# SEARCH 
# to render the search form
@app.route('/coffeegonewild/search')
def serach_for_recipe():
    return render_template("recipe_search.html")

# action route to get serach results
@app.route("/coffeegonewild/Iamready", methods=['POST'])
def search():
    session.clear()
    if not Recipe.validate(request.form):
        return redirect("/coffeegonewild/search")
    list_of_recipe_ids = Recipe.search(request.form)
    if len(list_of_recipe_ids)<1:
        return redirect("/coffeegonewild/search")
    session['list_of_recipe_ids'] = list_of_recipe_ids
    return redirect('/coffeegonewild/searchresult')

# action route to show search result
@app.route('/coffeegonewild/searchresult')
def serach_result():
    recipes = []
    for id in session['list_of_recipe_ids']:
        data = {
            'id':id
        }
        recipe = Recipe.get_one(data)
        recipes.append(recipe)
    return render_template('recipes_list.html', recipes = recipes)