from .base import Model
from sqlalchemy import Integer, String, Column
from flask_marshmallow import Schema


class Category(Model):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False, unique=True)

    def __repr__(self):
        return '<id: {} - name: {}>'.format(self.id, self.name)


class CategorySchema(Schema):
    class Meta:
        fields = ('id', 'name')
        model = Category


categories_schema = CategorySchema(many=True)
category_schema = CategorySchema()


def dump(data):
    if isinstance(data, list):
        return categories_schema.dump(data)
    return category_schema.dump(data)
