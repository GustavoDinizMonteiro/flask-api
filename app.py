from flask import Flask
from flask_cors import CORS
from flask_compress import Compress
from flasgger import Swagger
from dotenv import load_dotenv
from bookmark.controllers import register_routes
from bookmark.models import init_DB

load_dotenv()

app = Flask(__name__)
Compress(app)
CORS(app)
Swagger(app)
register_routes(app)

init_DB()
