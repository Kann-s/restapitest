from app import db
import json


class Product(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    product_code = db.Column(db.String(10), index=True, unique=True)
    product_name = db.Column(db.String(120), index=True)
    price = db.Column(db.Float)

    def __repr__(self):
        return json.dumps({
            'Product': {
                'id': self.id,
                'code': self.product_code,
                'name': self.product_name,
                'price': self.price
            }
        })
