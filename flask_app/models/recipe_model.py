from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import user_model
from flask_app.models import comment_model

class Recipe:
    def __init__(self , data):
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.temperature = data['temperature']
        self.creaminess = data['creaminess']
        self.sweetness = data['sweetness']
        self.with_foam = data['with_foam']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.image_link = data['image_link']


    # READ ALL METHOD
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL(DATABASE).query_db(query)
        all_recipes = []
        for row_from_db in results:
            recipe_instance = cls(row_from_db)
            all_recipes.append(recipe_instance)
        return all_recipes
    
    # READ ONE METHOD
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM recipes LEFT JOIN comments ON recipes.id = recipe_id LEFT JOIN users ON user_id = users.id where recipes.id = %(id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if len(results) < 1:
            return False
        else: 
            recipe_instance = cls(results[0])
            all_comments = []
            for row in results:
                if row['content']:
                    comment_data = {
                        **row,
                        'id': row['comments.id'],
                        'created_at': row['comments.created_at'],
                        'updated_at': row['comments.updated_at']
                    }
                    comment_instance = comment_model.Comment(comment_data)
                    all_comments.append(comment_instance)
                    
                    user_data = {
                            **row,
                            'id': row['users.id'],
                            'created_at': row['users.created_at'],
                            'updated_at': row['users.updated_at']
                        }
                    user_instance = user_model.User(user_data)
                    comment_instance.commenter = user_instance
            recipe_instance.list_of_comments = all_comments
        return recipe_instance
    
    # SEARCH
    @classmethod
    def search(cls, data):
        query = "SELECT id FROM recipes where temperature = %(temperature)s AND creaminess = %(creaminess)s AND sweetness = %(sweetness)s AND with_foam = %(with_foam)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        print(results)
        if len(results) < 1:
            flash('Sorry, we do not currently have something as special as you requested. Please try again.', "notfound") 
            return results
        else:
            list_of_recipe_ids = [] 
            for row in results:
                list_of_recipe_ids.append(row['id'])
            print(list_of_recipe_ids)
            return list_of_recipe_ids
    
    # get the average score of the comments and total comment count for this recipe
    @classmethod
    def calculate_avg_count(cls, data):
        query = "SELECT COALESCE(avg(rating), 0) as avg_rating, count(rating) as review_count FROM coffeegonewild.comments where recipe_id= %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results

    # Validator
    @staticmethod
    def validate(data):
        is_valid = True
        if 'temperature' not in data:
            is_valid = False
        if 'creaminess' not in data:
            is_valid = False
        if 'sweetness' not in data:
            is_valid = False
        if 'with_foam' not in data:
            is_valid = False
        if is_valid == False:
            flash('All fields required', 'reg')
        return is_valid