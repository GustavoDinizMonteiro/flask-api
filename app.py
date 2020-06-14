from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from bookmark.controllers import categories_resource, books_recource, comments_resource
from bookmark.models import init_DB

load_dotenv()

app = Flask(__name__)
CORS(app)

app.register_blueprint(categories_resource, url_prefix='/categories')
app.register_blueprint(books_recource, url_prefix='/books')
app.register_blueprint(comments_resource, url_prefix='/books/<book_id>/comments')
init_DB()
