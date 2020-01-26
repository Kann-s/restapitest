from app.api import bp
from app.models import Product

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
    return {}

@bp.route('/product/<int:id>', methods=['PUT'])
def update_product():
    return {}

@bp.route('/product/<int:id>', methods=['DELETE'])
def delete_product():
    return {}
