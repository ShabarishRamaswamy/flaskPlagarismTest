import json
import os
import time
from datetime import datetime, timedelta

import waitress
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

@app.route('/')

def trending():
   render_template('home.html', info="")

if __name__ == "__main__":
     app.debug = False
     port = int(os.environ.get('PORT', 33507))
     waitress.serve(app, port=port)
