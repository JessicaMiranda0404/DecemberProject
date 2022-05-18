from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Quote:
    db_name ="myquotes"
    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.quote = data['quote']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def save(cls,data):
        query = "INSERT INTO quotes (title, quote, user_id) VALUES(%(title)s,%(quote)s,%(user_id)s)"
        return connectToMySQL(cls.db_name).query_db(query,data)    

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM quotes;"
        results = connectToMySQL(cls.db_name).query_db(query)
        quotes = []
        for row in results:
            quotes.append( cls(row))
        return quotes

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM quotes WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        return cls( results[0] )

    #Not working need to fix
    @classmethod
    def update(cls, data):
        query = "UPDATE quotes SET title=%(title)s, quote=%(quote)s, updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)

    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM quotes WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)

    @staticmethod
    def validate_quote(quote):
        is_valid = True
        if len(quote['title']) < 2:
            is_valid = False
            flash("Name must be at least 2 characters")
        if len(quote['quote']) < 4:
            is_valid = False
            flash("Quotes must be at least 4 characters")
        return is_valid

    @classmethod
    def join_userquote(cls,data):
        query = "SELECT users.first_name as creator, quotes.* FROM users JOIN quotes;"
        results = connectToMySQL(cls.db_name).query_db(query)
        quotes = []
        for row in results:
            quotes.append(cls(row))
        print (...)
        return quotes.user.first_name 




# #Recent addition
#     @classmethod
#         def get_quote_with_favorites( cls , data ):
#             query = "SELECT * FROM quotes LEFT JOIN add_ons ON add_ons.quote_id = quotes.id LEFT JOIN favorites ON add_ons.favorite_id = favorites.id WHERE quotes.id = %(id)s;"
#             results = connectToMySQL('quotes').query_db( query , data )
#             # results will be a list of favorite objects with the quote attached to each row. 
#             quote = cls( results[0] )
#             for row_from_db in results:
#                 # Now we parse the favorite data to make instances of favorites and add them into our list.
#                 favorite_data = {
#                     "id" : row_from_db["favorites.id"],
#                     "quote_id" : row_from_db["quote_id"],
#                     "created_at" : row_from_db["favorites.created_at"],
#                     "updated_at" : row_from_db["favorites.updated_at"]
#                 }
#                 quote.favorites.append( favorite.favorite( favorite_data ) )
#             return quote