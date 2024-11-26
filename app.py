from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index', methods=["GET"])
def index():
    return render_template('index.html')

@app.route('/add')
def add():
    products = [
        {"name": "Laptop", "price": "250000 Ft", "category": "Elektronika"},
        {"name": "Fotel", "price": "50000 Ft", "category": "Bútor"},
        {"name": "Okosóra", "price": "75000 Ft", "category": "Elektronika"}
    ]
    return render_template('index.html', products=products)

@app.route('/add', methods=["GET", "POST"])
def add_products():
    if request.method == "POST":
        _name = request.form.get("name")
        _price = request.form.get("price")
        _category = request.form.get("category")
        product ={
            "name": _name,
            "price": _price,
            "category": _category,}
        products.append(product)
        print(product)
        return redirect(url_for('index'))
    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)
