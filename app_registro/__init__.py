from flask import Flask

app = Flask(__name__)

from app_registro.routes import *

# inicializar el servidor flask
# en mac export: FLASK_APP=main.py
# en windows: set FLASK_APP=main.py

# flask --app main --debug run