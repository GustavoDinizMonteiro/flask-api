from unittest import TestCase
from app import app
from bookmark.models import drop_DB, init_DB


class TestBooksResource(TestCase):
    def setUp(self):
        self.app = app.test_client()
        init_DB()
        self.mock_book = {
            'title': 'Scherlock',
            'author': 'Arthur',
            'description': 'Investigation'
        }

    def tearDown(self):
        drop_DB()

    def test_list(self):
        response = self.app.get('/books')
        self.assertEqual(200, response.status_code)

    def test_create(self):
        response = self.app.post('/books', json=self.mock_book)
        self.assertEqual(200, response.status_code)
