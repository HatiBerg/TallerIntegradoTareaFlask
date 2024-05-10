from flask import Flask, jsonify, render_template
import json
import random

app = Flask(__name__)

with open('C:/Users/resid/GitHub/TallerIntegradoTareaFlask/static/vgsales.json', 'r') as j:
  data = json.load(j)

def random_platform():
  platform = set(game['platform'] for game in data)
  rd_platform = random.choice(list(platform))
  return rd_platform

def random_genre():
  genres = set(game['genre'] for game in data)
  rd_genre = random.choice(list(genres))
  return rd_genre

@app.route("/")
def index():
  return render_template("index.html", data=data)

@app.route("/platform/<string:slug>/")
def plataformas(slug):
    return render_template("plataformas.html", data=data, random_platform=random_platform(), slug_platform=slug)

@app.route("/genre/<string:slug>/")
def generos(slug):
    return render_template("generos.html", data=data, random_genre=random_genre(), slug_genre=slug)
