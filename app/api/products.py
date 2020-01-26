from app.api import bp


@bp.route('/products', methods=['GET'])
def get_products():
    return {}

@bp.route('/product/<int:id>', methods=['GET'])
def get_product(id):
    return {}

@bp.route('/product', methods=['POST'])
def create_product():
    return {}

@bp.route('/product/<int:id>', methods=['PUT'])
def update_product():
    return {}

@bp.route('/product/<int:id>', methods=['DELETE'])
def delete_product():
    return {}
