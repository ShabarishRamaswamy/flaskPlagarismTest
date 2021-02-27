import json
import os
import time
# import plagiarism
from waitress import serve

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
app.debug = True

# Home Route
@app.route('/')
def homeRoute():
   return "Hello World"

# Values Input Route
@app.route("/input", methods=['POST'])
def inputValues():
       userInput = request.get_json(silent=True)
       print(userInput)
       return userInput


@app.route("/output", methods=['GET'])
def outputValues():
   userOutput = 0
   if(userOutput):
      return "Hello"
   return "Hello"


if __name__ == "__main__":
      #  port = process.env.PORT || 8080
       serve(app, host="0.0.0.0", port = 8080)
       
