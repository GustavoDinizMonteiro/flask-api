from .base import Model
from sqlalchemy import Integer, String, Column
from dataclasses import dataclass


@dataclass
class Category(Model):
    __tablename__ = 'category'

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String(80), nullable=False, unique=True)

    def __repr__(self):
        return '<id: {} - name: {}>'.format(self.id, self.name)
