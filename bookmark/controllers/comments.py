from flask import Blueprint, jsonify, request
from bookmark.models import session
from bookmark.models.comment import Comment

comments_resource = Blueprint('comments', __name__)


@comments_resource.route('', methods=['POST'])
def create(book_id):
    comment = Comment(**request.get_json(), parent_id=book_id)
    session.add(comment)
    session.commit()
    return jsonify(comment)