from unittest import TestCase
from fastapi.testclient import TestClient
from app.main import app as web_app


class ApiTestCase(TestCase):

    def setUp(self):
        self.client = TestClient(web_app)

    def test_main_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 404)

    def test_create_user(self):
        user_data = {
            'user': {
                'email': 'test1@test.com',
                'password': '12345',
                'first_name': 'Anna',
                'last_name': 'Halii',
                'nickname': 'halli22'
            }
        }

        responce = self.client.post('/user', json=user_data)
        self.assertEqual(responce.status_code, 200)

