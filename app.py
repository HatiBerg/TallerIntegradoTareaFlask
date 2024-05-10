from flask import Flask, redirect, render_template, url_for
import json
import random

app = Flask(__name__)

with open('C:/Users/resid/GitHub/TallerIntegradoTareaFlask/static/vgsales.json', 'r') as j:
  data = json.load(j)

def get_all_platforms():
    platforms = set(game['platform'] for game in data)
    return list(platforms)
platforms = get_all_platforms()

def get_all_genres():
    genres = set(game['genre'] for game in data)
    return list(genres)
genres = get_all_genres()

@app.route("/")
def index():
  return render_template("index.html", data=data)

@app.route("/platform/")
def plataformas():
    random_platform = random.choice(platforms)
    return redirect(url_for('plataforma_randon', slug=random_platform))

@app.route("/platform/<string:slug>/")
def plataforma_randon(slug):
    return render_template("plataformas.html", data=data, random_platform=slug)

@app.route("/genre/")
def generos():
  random_genre = random.choice(genres)
  return redirect(url_for('genero_randon', slug=random_genre))

@app.route("/genre/<string:slug>/")
def genero_randon(slug):
    return render_template("generos.html", data=data, random_genre=slug)
