from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

products = [
    {"name": "Laptop", "price": "250000 Ft", "category": "Elektronika"},
    {"name": "Fotel", "price": "50000 Ft", "category": "Bútor"},
    {"name": "Okosóra", "price": "75000 Ft", "category": "Elektronika"}
]

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/add', methods=["GET", "POST"])
def add_products():
    if request.method == "POST":
        _name = request.form.get("name")
        _price = request.form.get("price")
        _category = request.form.get("category")
        
        if _name and _price and _category:
            product = {
                "name": _name,
                "price": _price,
                "category": _category,
            }
            products.append(product)
            print(f"Új termék hozzáadva: {product}")
            return redirect(url_for('index'))
        else:
            print("Hibás adatbevitel, kérem, minden mezőt töltsön ki!")
    
    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)
