from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.quote import Quote
from flask_app.models.user import User

#New Quote page working
@app.route('/new/quote')
def new_quote():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['user_id']
    }
    return render_template('new_quote.html',user=User.get_by_id(data))

@app.route('/create/quote',methods=['POST'])
def create_quote():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Quote.validate_quote(request.form):
        return redirect('/new/quote')
    data = {
        "title": request.form["title"],
        "quote": request.form["quote"],
        "user_id": session["user_id"]
    }
    Quote.save(data)
    return redirect('/dashboard')

@app.route('/quotes/<int:id>')
def quotes():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    return render_template("quotes.html",quote=Quote.get_one(data),user=User.get_by_id(user_data))


@app.route('/destroy/quote/<int:id>')
def destroy_quote(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Quote.destroy(data)
    return redirect('/dashboard')

#Adding 12/10
@app.route('/edit/quote/<int:id>')
def edit_quote(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("edit_quote.html",quote=Quote.get_one(data),user=User.get_by_id(user_data))










@app.route('/update/quote',methods=['POST'])
def update_quote():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Quote.validate_quote(request.form):
        return redirect('/new/quote')
    data = {
        "title": request.form["title"],
        "quote": request.form["quote"],
        "user_id": session["user_id"]
    }
    Quote.save(data)
    return redirect('/dashboard')