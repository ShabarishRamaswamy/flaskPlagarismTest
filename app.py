import json
import os
import time

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

# Home Route
@app.route('/')
def trending():
   return render_template('home.html', info="")

# Values Input Route
@app.route('/input/<id>', methods=['POST'])
def inputValues():
   pass


@app.route('/output/<id>', methods=['GET'])
def outputValues():
   pass


if __name__ == "__main__":
    app.run()
