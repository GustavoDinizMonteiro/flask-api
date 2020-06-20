from flask import Blueprint, jsonify, request
from flasgger.utils import swag_from
from bookmark.models import session
from bookmark.models.book import Book
from docs.swagger.book_specs import create_specs, list_specs

books_recource = Blueprint('books', __name__)


@books_recource.route('', methods=['POST'])
@swag_from(create_specs)
def create():
    """
    Create a new book.
    ---
    """
    book = Book(**request.get_json())
    session.add(book)
    session.commit()
    return jsonify(book)


@books_recource.route('', methods=['GET'])
@swag_from(list_specs)
def list():
    """
    List all books.
    ---
    """
    books = session.query(Book).all()
    return jsonify({'books': books})
