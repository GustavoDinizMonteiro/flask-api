from flask import Blueprint, jsonify, request
from bookmark.models import session
from bookmark.models.book import Book

books_recource = Blueprint('books', __name__)


@books_recource.route('', methods=['POST'])
def create():
    book = Book(**request.get_json())
    session.add(book)
    session.commit()
    return book


@books_recource.route('', methods=['GET'])
def list():
    books = session.query(Book).all()
    return jsonify({ 'books': books })