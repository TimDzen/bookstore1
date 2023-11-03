from flask import g

from app.infra.storage.repository import BookRepository
from app.application.book_service import BookService


class Context:
    def __init__(self):
        book_repository = BookRepository('sqlite:///bookstore.db')
        self.book_service = BookService(book_repository)


def get_context(app):
    return app.config["CONTEXT"]


