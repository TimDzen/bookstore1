from flask import Flask
from sqlalchemy import create_engine

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookstore.db'
db_engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])

from app.infra.storage.repository import BookRepository

book_repository = BookRepository(db_engine)
