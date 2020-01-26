# restapitest
This application implements a sample RESTful API using Python and Flask

### Introduction

Implemented a simple back-end service for an online marketplace.  Here is a sample of some of the products available on the site.

| Product code  | Name  |  Price |
|---|---|---|
|  001 |  Lavender heart | £9.25  |
|  002 |  Personalised cufflinks | £45.00  |
|  003 |  Kids T-shirt | £19.95 |

The RESTful API implements CRUD operations on this data.  The following five endpoints are provided:

* GET /products - A list of products, names, and prices in JSON.
* POST /product - Create a new product from a JSON body.
* GET /product/{product_id} - Return a single product by id in JSON.
* PUT /product/{product_id} - Update a product's name or price by id.
* DELETE /product/{product_id} - Delete a product by id.

### Implementation

The service is implemented in Python using Flask framework. It returns sensible status codes in the response for both successful and unsuccessful requests.

It uses SQLite database for persistence and Flask-SQLAlchemy as the ORM.

### Install instructions

C:\Users\sriram\dev\pydev>git clone https://github.com/Kann-s/restapitest.git

cd restapitest

python -m venv venv

venv\Scripts\activate

pip install flask
pip install flask-sqlalchemy
pip install flask-migrate
pip install python-dotenv

* All the above libraries can be installed using the command:

(venv) $ pip install -r requirements.txt

* create the database using the command

flask db upgrade

* Seed data can be imported into the application using the command

python seed_data.py

* Application can be run using the command

flask run

* Tests can be run using the command:

python tests.py

Please note that the postman tests are not yet included into the above tests.py module.

* Please seed the database as above before running the postman tests.

### Notes and suggestions

* Postman tests all succeed except for the POST /v1/products to create a product. This test expects a 200 status code, whereas the application returns 201 Created, which I believe is correct. So didn't change to make the test pass.
