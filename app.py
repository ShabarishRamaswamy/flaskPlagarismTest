import json
import os
import time
from waitress import serve

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
app.debug = True

userOutput = {}
# Home Route
@app.route('/')
def homeRoute():
   return "Hello World"

# Values Input Route
@app.route("/input", methods=['POST'])
def inputValues():
       from plagiarism import givejson
       userInput = request.get_json(silent=True)
       userOutput = givejson(userInput)
       return userInput


@app.route("/output", methods=['GET'])
def outputValues():
   if(userOutput != 0):
      return userOutput
   return "Value has not been computed"


if __name__ == "__main__":
       port = os.environ.get('PORT')
       if(port):
               serve(app)
       else:
         serve(app, host="0.0.0.0", port = 8080)