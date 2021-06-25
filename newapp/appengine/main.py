#hello
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
  return '<body bgcolor="#FFFF00"><center><h1>I am the AppEngine App. Version - 2</h1></center></body>'
