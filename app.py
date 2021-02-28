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
       l=''
       for x,y in userOutput.items():
           l = l +" "+x+"\t"+y+" "+"\n"
       if not userInput == False:
           return l


@app.route("/output", methods=['GET'])
def outputValues():
   k = inputValues()
   if(userOutput != 0):
      return k
   return "Value has not been computed"


if __name__ == "__main__":
       app.run()
