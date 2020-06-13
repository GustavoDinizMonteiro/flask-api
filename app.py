from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from bookmark.controllers import categories_resource
from bookmark.models import init_DB

load_dotenv()

app = Flask(__name__)
CORS(app)

app.register_blueprint(categories_resource, url_prefix='/categories')
init_DB()
