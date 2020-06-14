from .categories import categories_resource
from .books import books_recource
from .comments import comments_resource


def register_routes(app):
    app.register_blueprint(categories_resource, url_prefix='/categories')
    app.register_blueprint(books_recource, url_prefix='/books')
    app.register_blueprint(
        comments_resource, url_prefix='/books/<book_id>/comments'
    )
