from .. import app
from flask import render_template

@app.route("/")
def index():    
    return render_template("menu.html", title="Zmiini Novatori")


@app.route("/ourhobbies")
def ourhobbies():
    ourhobbies = [
        ("Leonid:", " Football, Programming, Gym"),
        ("Bohdan:", " Programming, Gym, Games"),
        ("Nazar:", " Chess, Table Tennis, Programming"),
        ("Oleksandr:", " Programming, Games, Gym"),
    
    ]
    context = {
        "ourhobbies" : ourhobbies,
    }
    return render_template("ourhobbies.html", **context)


@app.route("/goodandbad")
def goodbad():
    goodandbad = [
        ("Good: ", "Teamwork, Time Management, Knowledge"),
        ("Bad: ", "404 Not Found")
    
    ]
    context = {
        "goodandbad" : goodandbad,
    }
    return render_template("goodandbad.html", **context)