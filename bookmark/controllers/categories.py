from flask import Blueprint, jsonify, request
from flasgger.utils import swag_from
from bookmark.models import session
from bookmark.models.category import Category
from docs.swagger.category_specs import list_specs

categories_resource = Blueprint('categories', __name__)


@categories_resource.route('', methods=['GET'])
@swag_from(list_specs)
def get():
    categories = session.query(Category).all()
    return jsonify({'categories': categories})
