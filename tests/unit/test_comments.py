from unittest import TestCase
from app import app
from bookmark.models import drop_DB, init_DB

class TestCommentsResource(TestCase):
    def setUp(self):
        self.app = app.test_client()
        init_DB()
    

    def tearDown(self):
        drop_DB()

    def test_list(self):
        pass