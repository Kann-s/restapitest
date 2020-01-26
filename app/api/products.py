from app.api import bp
from app.models import Product
from app import db
from app.api.errors import bad_request

from flask import jsonify
from flask import request

@bp.route('/products', methods=['GET'])
def get_products():
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 100)
    data = Product.to_collection_dict(Product.query, page, per_page)
    return jsonify(data)

@bp.route('/product/<int:id>', methods=['GET'])
def get_product(id):
    return jsonify(Product.query.get_or_404(id).to_dict())

@bp.route('/product', methods=['POST'])
def create_product():
    data = request.get_json() or {}
    if 'name' not in data or 'price' not in data:
        return bad_request('must include Product name and price fields')
    product = Product()
    product.from_dict(data)
    db.session.add(product)
    db.session.commit()
    response = jsonify(product.to_dict())
    response.status_code = 201
    return response

@bp.route('/product/<int:id>', methods=['PUT'])
def update_product():
    return {}

@bp.route('/product/<int:id>', methods=['DELETE'])
def delete_product():
    return {}
