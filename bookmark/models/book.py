from datetime import datetime
from dataclasses import dataclass
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Integer, Column, String, Text,
    Boolean, ForeignKey, DateTime
)
from .base import Model
from .category import Category

@dataclass
class Book(Model):
    __tablename__ = 'book'
    id: int = Column(Integer, primary_key=True)
    title: str = Column(String(50), nullable=False, unique=True)
    description: str = Column(Text)
    author: str = Column(String(50), nullable=False)

    deleted: bool = Column(Boolean, default=False)
    created_date: datetime = Column(DateTime, default=datetime.now)

    category_id: int = Column(Integer, ForeignKey('category.id'))
    category: Category = relationship('Category')

    def __repr__(self):
        return '<id: {} - name: {} - category: {}>'.format(
            self.id, self.title, self.category_id
        )

