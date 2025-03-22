# app/tests/test_routes.py
import unittest
from app import app

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to the Self-Healing Network Security System', response.data)

    def test_isolate_route(self):
        response = self.app.post('/api/isolate_node/101')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Device 101 isolated successfully', response.data)

    def test_heal_route(self):
        response = self.app.post('/api/heal_node/101')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Device 101 healed successfully', response.data)

if __name__ == '__main__':
    unittest.main()
