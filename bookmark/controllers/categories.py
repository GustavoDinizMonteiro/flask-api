from flask import Blueprint, jsonify, request
from bookmark.models import session
from bookmark.models.category import Category

categories_resource = Blueprint('categories', __name__)


@categories_resource.route('', methods=['GET'])
def get():
    categories = session.query(Category).all()
    return jsonify({'categories': categories})


@categories_resource.route('/<id>', methods=['GET'])
def get_by_id(id):
    category = session.query(Category).get(id)
    return jsonify(category)
