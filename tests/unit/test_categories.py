from unittest import TestCase
from app import app
from bookmark.models import drop_DB, init_DB


class TestCategoriesResource(TestCase):
    def setUp(self):
        self.app = app.test_client()
        init_DB()

    def tearDown(self):
        drop_DB()

    def test_list(self):
        response = self.app.get('/categories')
        self.assertEqual(200, response.status_code)
