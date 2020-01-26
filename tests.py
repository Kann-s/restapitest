import unittest
from app import create_app, db
from app.models import Product
from config import Config

import seed_data


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


class ProductModelCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_products(self):
        products = Product.query.all()
        for p in products:
            print(p)
        self.assertEqual(1,1, '1 = 1')


if __name__ == "__main__":
    unittest.main()
