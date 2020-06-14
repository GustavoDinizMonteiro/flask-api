from flask import Blueprint, jsonify, request
from flasgger.utils import swag_from
from bookmark.models import session
from bookmark.models.comment import Comment
from docs.swagger.comment_specs import create_specs

comments_resource = Blueprint('comments', __name__)


@comments_resource.route('', methods=['POST'])
@swag_from(create_specs)
def create(book_id):
    """
    Create comment associated to book.
    ---
    """
    comment = Comment(**request.get_json(), parent_id=book_id)
    session.add(comment)
    session.commit()
    return jsonify(comment)
