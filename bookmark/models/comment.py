from datetime import datetime
from dataclasses import dataclass
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Integer, Column, String, Text,
    Boolean, ForeignKey, DateTime
)
from .base import Model


@dataclass
class Comment(Model):
    __tablename__ = 'comment'
    id: int = Column(Integer, primary_key=True)

    author: str = Column(String(50), nullable=False)
    body: str = Column(Text)

    deleted: bool = Column(Boolean, default=False)
    timestamp: datetime = Column(DateTime, default=datetime.now)

    parent_id: int = Column(Integer, ForeignKey('book.id'))
    book = relationship('Book', back_populates='comments')

    def __repr__(self):
        return '<id: {} - author: {}'.format(self.id, self.author)
