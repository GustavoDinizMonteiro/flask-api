from flask import Blueprint, jsonify, request
from bookmark.models import session
from bookmark.models.book import Book, dump

books_recource = Blueprint('books', __name__)


@books_recource.route('', methods=['POST'])
def create():
    book = Book(**request.get_json())
    session.add(book)
    session.commit()
    return dump(book)


@books_recource.route('', methods=['GET'])
def list():
    query = session.query(Book).all()
    return jsonify({ 'books': dump(query) })