from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*[0-9])(?=.*[A-Z])(.{8,100})$')
ALPHANUMERIC = re.compile(r"^[a-zA-Z0-9]+$") 

class User:
    def __init__(self , data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.user_name = data['user_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    #CREATE ONE
    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (first_name, last_name, user_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(user_name)s, %(email)s, %(password)s);"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results

    # CHECK USER NAME
    @classmethod
    def get_by_user_name(cls,data):
        query = "SELECT * FROM users WHERE user_name = %(user_name)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])
    
    # CHECK EMAIL
    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    # Validator
    @staticmethod
    def validate(data):
        # can use print(data) to check what kind of data we get back
        is_valid = True
        if len(data['first_name']) < 2:
            is_valid = False
            flash('First name must be at least 2 characters', 'reg')
        elif not ALPHANUMERIC.match(data['first_name']):
            flash('First name cannot contain special chars', 'reg')
            is_valid = False
        if len(data['last_name']) < 2:
            is_valid = False
            flash('Last name must be at least 2 characters', 'reg')
        elif not ALPHANUMERIC.match(data['last_name']):
            flash('Last name cannot contain special chars', 'reg')
            is_valid = False
        if len(data['user_name']) < 2:
            is_valid = False
            flash('User name must be at least 2 characters', 'reg')
        else:
            data2 = {
                'user_name': data['user_name']
            }
            potential_user = User.get_by_user_name(data2)
            if potential_user:
                is_valid = False
                flash("User name already taken. Please try something else", 'reg' )
        if len(data['email']) < 2:
            is_valid = False
            flash('Please provide valid email', 'reg')
        elif not EMAIL_REGEX.match(data['email']): 
            flash('Invalid email address!', 'reg')
            is_valid = False
        else:
            data3 = {
                'email': data['email']
            }
            potential_user = User.get_by_email(data3)
            if potential_user: #if we have a user, don't let them register with this email.
                is_valid = False
                flash("Email already in DB, hope it's you...", 'reg')
        if len(data['password']) < 8:
                is_valid = False
                flash('Password must be at least 8 chars', 'reg') 
        elif not PASSWORD_REGEX.match(data['password']): 
            flash('Password must contain at least one number and one uppercase letter', 'reg')
            is_valid = False
        elif not data['password'] == data['confirmed_password']:
                is_valid = False
                flash("Password don't match", 'reg')
        return is_valid