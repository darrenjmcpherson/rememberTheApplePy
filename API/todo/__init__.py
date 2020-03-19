from flask import Flask
from todo.main.controllers import main

app = Flask(__name__)

app.register_blueprint(main, url_prefix='/')