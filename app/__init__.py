from flask import Flask


app = Flask(__name__)
app.template_folder = "../templates/"
app.static_folder = "../static/"

from . import routes


