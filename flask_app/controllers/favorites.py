from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.quote import Quote
from flask_app.models.user import User
from flask_app.models.favorite import Favorite 

@app.route('/favorite')
def new_favorite():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['user_id']
    }
    return render_template("favorite.html", quote=Quote.get_one(data),user=User.get_by_id(user_data))

@app.route('/add/favorite/<int:id>')
def add_favorite(id):
    if 'user_id' not in session:
        return redirect('/logout')

    data = {
   
        "user_id": session["user_id"],
        "quote_id": id
    }
    Favorite.favorite_quote(data)
    return redirect('/personal/dashboard')