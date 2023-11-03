from app.domain.book import Book
from sqlalchemy.orm import sessionmaker

class BookRepository:
    def __init__(self, db_engine):
        self.db_engine = db_engine
        self.Session = sessionmaker(bind=db_engine)

    def get_all(self):
        session = self.Session()
        books = session.query(Book).all()
        session.close()
        return books

    def add(self, book):
        session = self.Session()
        session.add(book)
        session.commit()
        session.close()