from .category import Category
from .book import Book
from .base import Session, engine, Model

session = Session()


def init_DB():
    Model.metadata.create_all(engine)
