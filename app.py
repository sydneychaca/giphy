# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask, render_template, request
from datetime import datetime
from model import getImageUrlFrom
import os

# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", time = datetime.now())

# add route for your gif results
@app.route('/yourgif', methods = ["GET","POST"])
def yourgif(): #name here does not matter but usually name of route
    #get the giph for giphy and puts the link on webpage
    user_response = request.form["gifchoice"]
    #user_response = "dog"
    gif_link = getImageUrlFrom(user_response)
    print(gif_link)
    #pass URL to render template and have that URL appear as an image in yourgof.html
    return render_template("yourgif.html", time = datetime.now(), gif_link = gif_link)
    #add datetime.now() to trick our browser into updating the css