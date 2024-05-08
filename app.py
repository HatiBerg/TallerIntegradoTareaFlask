from flask import Flask, render_template

app = Flask(__name__)

@app.route("")
def index():
    return render_template("index.html")

# @app.route("/<string:slug>/")
# def def1(slug):
#     return render_template("template1.html", slug_title=slug)

# @app.route("/<string:slug>/")
# def def2(slug):
#     return render_template("template2.html", slug_title=slug)