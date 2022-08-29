from dataclasses import dataclass
from flask_app import app
from flask import render_template, redirect, request, flash, session
from flask_app.models.user_model import User
from flask_app.models.recipe_model import Recipe

# READ ALL ROUTE
@app.route("/coffeegonewild/all_recipes")
def all_recipes():
    # call the get all classmethod to get all friends
    all_recipes = Recipe.get_all()
    # print(all_recipes)
    return render_template("recipes_all.html", all_recipes = all_recipes)

# READ ONE
@app.route("/coffeegonewild/viewrecipe/<int:id>")
def view_recipe(id):
    # if not "user_id" in session:
    #     return redirect('/')
    data = {
        'id': id
    }
    session['recipe_id'] = id
    recipe = Recipe.get_one(data)
    return render_template("recipe_one.html", recipe = recipe)

# SEARCH 
# to render the search form
@app.route('/coffeegonewild/search')
def serach_for_recipe():
    return render_template("recipe_search.html")

# action route to get serach results
@app.route("/coffeegonewild/Iamready", methods=['POST'])
def search():
    print(request.form)
    session.clear()
    if not Recipe.validate(request.form): #need to add the validator
        return redirect("/coffeegonewild/search")
    list_of_recipe_ids = Recipe.search(request.form)
    print(list_of_recipe_ids)
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
        print(recipes)
        # session.pop(['list_of_recipe_ids'])
    return render_template('recipes_list.html', recipes = recipes)

# # COMMENT
# @app.route('/coffeegonewild/add_comment', methods=['POST'])
# def add_comment():
#     if not "user_id" in session:
#         return redirect('login.html')
    
    