from json import loads
from unittest import TestCase
from app import app
from bookmark.models import drop_DB, init_DB


class TestCommentsResource(TestCase):
    def setUp(self):
        self.app = app.test_client()
        init_DB()
        self.mock_book = {
            'title': 'Scherlock',
            'author': 'Arthur',
            'description': 'Investigation'
        }
        self.mock_comment = {
            'author': 'Gustavo Monteiro',
            'body': 'Muito bom'
        }
        self.mock_comment2 = {
            'author': 'Andy Monteiro',
            'body': 'Maravilhoso!'
        }

    def tearDown(self):
        drop_DB()

    def get_body(self, request):
        return loads(request.get_data(as_text=True))

    def test_create(self):
        book_response = self.app.post('/books', json=self.mock_book)
        book = self.get_body(book_response)

        comment_response = self.app.post(
            '/books/{}/comments'.format(book['id']),
            json=self.mock_comment
        )
        self.assertEqual(200, comment_response.status_code)

        comment = self.get_body(comment_response)
        self.assertEqual(self.mock_comment['author'], comment['author'])
        self.assertEqual(self.mock_comment['body'], comment['body'])
        self.assertEqual(book['id'], comment['parent_id'])
        self.assertNotEqual(comment['id'], None)

    def test_list(self):
        book_response = self.app.post('/books', json=self.mock_book)
        book = self.get_body(book_response)
        self.app.post(
            '/books/{}/comments'.format(book['id']),
            json=self.mock_comment
        )
        self.app.post(
            '/books/{}/comments'.format(book['id']),
            json=self.mock_comment2
        )

        response = self.app.get('/books')
        self.assertEqual(200, response.status_code)

        response_data = self.get_body(response)
        self.assertNotEqual(response_data['books'], None)
        self.assertNotEqual(len(response_data['books']), 2)
