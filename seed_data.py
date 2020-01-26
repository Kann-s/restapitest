from app import create_app, db
from app.models import Product

def insert_product_test_data():
    print("Seeding Product table with sample data...", end="")
    p1 = Product(product_code='001', product_name='Lavender heart', price=9.25)
    p2 = Product(product_code='002', product_name='Personalised cufflinks', price=45.00)
    p3 = Product(product_code='003', product_name='Kids T-shirt', price=19.95)
    db.session.add_all([p1,p2,p3])
    db.session.commit()
    print("...done.")

if __name__ == "__main__":
    app = create_app()
    app_context = app.app_context()
    app_context.push()
    insert_product_test_data()
