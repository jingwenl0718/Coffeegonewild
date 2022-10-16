from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class Comment:
    def __init__(self , data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.recipe_id = data['recipe_id']
        self.content = data['content']
        self.name = data['name']
        self.rating = data['rating']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    #CREATE ONE
    @classmethod
    def create(cls, data):
        query = "INSERT INTO comments (user_id, recipe_id, name, content, rating) VALUES (%(user_id)s, %(recipe_id)s, %(name)s, %(content)s, %(rating)s);"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results
