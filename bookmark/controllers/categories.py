import os
from flask import Blueprint, jsonify, request
from bookmark.models import session
from bookmark.models.category import Category, dump

categories_resource = Blueprint('categories', __name__)


@categories_resource.route('', methods=['POST'])
def create():
    category = Category(name=request.json.get('name'))
    session.add(category)
    session.commit()
    return dump(category)


@categories_resource.route('', methods=['GET'])
def get():
    query = session.query(Category).all()
    return jsonify({'categories': dump(query)})


@categories_resource.route('/<id>', methods=['GET'])
def get_by_id(id):
    query = session.query(Category).get(id)
    return dump(query)
