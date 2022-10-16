from dataclasses import dataclass
from flask_app import app
from flask import request, session, jsonify
from flask_app.models.user_model import User
from flask_app.models.recipe_model import Recipe
from flask_app.models.comment_model import Comment

@app.route("/api/coffeegonewild/add_comment", methods=["POST"])
def api_create_comment():
    if not "user_id" in session:
        no_user_res = {
            'msg': 'NoUserError',
        }
        return jsonify(no_user_res)
    data = {
        'name': request.form['name'],
        'content': request.form['content'],
        'rating': request.form['rating'],
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
