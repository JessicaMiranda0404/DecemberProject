from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user 

class Favorite:
    db ="myquotes"
    def __init__( self , db_data ):
        self.id = db_data['id']
        self.user_id = db_data['user_id']
        self.quote_id = db_data['quote_id']
        self.on_quotes = []
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @classmethod
    def get_all(cls):
        query= "SELECT * FROM favorites LEFT JOIN users on users.id = user_id;"
        results = connectToMySQL(cls.db).query_db(query)
        print (f"RESULTS: {results}") 
        favorites= []
        for row in results: 

            user_data = {
                'id': row['users.id'],
                'first_name':row['first_name'],
                'last_name':row['last_name'],
                'email':row['email'],
                'password':row['password'],
                'created_at':row['created_at'],
                'updated_at':row['updated_at'],
            }

            new_favorite = cls(row)
            new_favorite.user = user.User(user_data)
            favorites.append(new_favorite)
        return favorites

    @classmethod
    def favorite_quote(cls,data):
        query = "insert into favorites (user_id, quote_id) values (%(user_id)s, %(quote_id)s);"
        return(connectToMySQL(cls.db).query_db(query,data))