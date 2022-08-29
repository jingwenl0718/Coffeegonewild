from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import user_model
from flask_app.models import recipe_model

class Comment:
    def __init__(self , data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.recipe_id = data['recipe_id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    #CREATE ONE
    @classmethod
    def create(cls, data):
        query = "INSERT INTO comments (user_id, recipe_id, content) VALUES (%(user_id)s, %(recipe_id)s, %(content)s);"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results