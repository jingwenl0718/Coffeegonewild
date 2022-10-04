from dataclasses import dataclass
from flask_app import app
from flask import render_template, redirect, request, flash, session, jsonify
from flask_app.models.user_model import User
from flask_app.models.recipe_model import Recipe
from flask_app.models.comment_model import Comment

# @app.route("/api/coffeegonewild/check_comment_user", methods=["POST"])
# def api_create_comment():
#     # print(request.form)
#     if not "user_id" in session:
#         # return redirect('/coffeegonewild/login_form')
#         # return render_template("login.html")
#         # return redirect("/coffeegonewild" )
#         # res = {}
#         return dict()
    
#     data = {
#         'content': request.form['content'],
#         'user_id': session['user_id'],
#         'recipe_id': session['recipe_id']
#     }
#     Comment.create(data)
#     res = {
#         'msg': 'success',
#         'form': data,
#         'user_name': session['user_name']
#     }
#     return jsonify(res)



@app.route("/api/coffeegonewild/add_comment", methods=["POST"])
def api_create_comment():
    if not "user_id" in session:
        return redirect('/coffeegonewild/login_form')
        # return render_template("login.html")
        # return redirect("/coffeegonewild" )
        # return ValueError('no user id yet!')
    data = {
        'content': request.form['content'],
        'user_id': session['user_id'],
        'recipe_id': session['recipe_id']
    }
    Comment.create(data)
    res = {
        'msg': 'success',
        'form': data,
        'user_name': session['user_name']
    }
    return jsonify(res)
