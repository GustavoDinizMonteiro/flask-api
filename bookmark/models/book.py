from datetime import datetime
from flask_marshmallow import Schema
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Integer, Column, String, Text,
    Boolean, ForeignKey, DateTime
)
from .base import Model
from .category import CategorySchema


class Book(Model):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False, unique=True)
    description = Column(Text)
    author = Column(String(50), nullable=False)

    deleted = Column(Boolean, default=False)
    created_date = Column(DateTime, default=datetime.now)

    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship('Category')

    def __repr__(self):
        return '<id: {} - name: {} - category: {}>'.format(
            self.id, self.title, self.category_id
        )


class BookSchema(Schema):
    class Meta:
        fields = (
            'id', 'title', 'description', 'author',
            'deleted', 'created_date', 'category_id'
        )
        model = Book
        include_fk = True

books_schema = BookSchema(many=True)
book_schema = BookSchema()


def dump(data):
    if isinstance(data, list):
        return books_schema.dump(data)
    return book_schema.dump(data)
