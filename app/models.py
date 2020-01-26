from app import db
import json


class PaginatedAPIMixin(object):
    @staticmethod
    def to_collection_dict(query, page, per_page):
        resources = query.paginate(page, per_page, False)
        data = [ item.to_dict() for item in resources.items ]
        return data

class Product(PaginatedAPIMixin, db.Model):

    id = db.Column(db.Integer, primary_key=True)
    product_code = db.Column(db.String(10), index=True, unique=True)
    product_name = db.Column(db.String(120), index=True)
    price = db.Column(db.Float)

    def to_dict(self):
        data = {
            'id': self.id,
            'name': self.product_name,
            'price': self.price,
        }
        return data

    def from_dict(self, data):
        field_to_cols_mapping = {
            'code': 'product_code',
            'name': 'product_name',
            'price': 'price'
        }
        for field in ['code', 'name', 'price']:
            if field in data:
                setattr(self, field_to_cols_mapping.get(field), data[field])

    def __repr__(self):
        return json.dumps({
            'Product': {
                'id': self.id,
                'code': self.product_code,
                'name': self.product_name,
                'price': self.price
            }
        })
