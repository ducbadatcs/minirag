# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template, redirect, url_for, request
from summarize import *

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return render_template("data_form.html")

@app.route("/summarize", methods = ["POST"])
def summarize():
    if request.method == "POST":
        text = request.form.get("text")
        return f"<p>{text}</p>"

# main driver function
if __name__ == '__main__':
    app.run(debug=True)