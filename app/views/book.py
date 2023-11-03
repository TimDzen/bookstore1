from flask import Blueprint, current_app, request, jsonify

from app.domain import book
from app.domain.book import Book
from app.infra.storage.repository import BookRepository

bp = Blueprint("book", __name__)
book_repository = current_app.book_repository


@bp.route("/")
def get_books():
    books = book_repository.get_all()
    return jsonify([{
        "id": book.id,
        "title": book.title,
        "author": book.author,
        "publish_year": book.publish_year
    } for book in books])


@bp.route("/", methods=["POST"])
def add_book():
    book_data = request.json
    book = Book(**book_data)
    book_repository.add(book)
    return jsonify({"id": book.id, "book": {
        "title": book.title,
        "author": book.author,
        "publish_year": book.publish_year
    }})


@bp.route('/book/<int:book_id>')
def get_by_id(id):
    id = Book.query.get_or_404(book, id)
    return jsonify({"id": book.id, "book": {
        "title": book.title,
        "author": book.author,
        "publish_year": book.publish_year
    }})
