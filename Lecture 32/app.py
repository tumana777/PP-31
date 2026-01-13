from flask import Flask, Response, render_template
app = Flask(__name__)

from models import products

# @app.route("/")
# def index():
#     return Response("<h1>This is main page</h1>")

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about/")
def about():
    return render_template('about.html')

@app.route("/products/")
def products_func():
    available_products = list(products.find({'is_available': True}))
    total_products = products.count_documents({'is_available': True})

    return render_template('products.html',
                           products=available_products,
                           total_products=total_products
                           )

if __name__ == '__main__':
    app.run(debug=True)