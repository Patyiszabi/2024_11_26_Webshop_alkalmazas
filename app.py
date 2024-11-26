from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')

@app.route('/home')
def tabla():
    products = [
        {"name": "Laptop", "price": "250000 Ft", "category": "Elektronika"},
        {"name": "Fotel", "price": "50000 Ft", "category": "Bútor"},
        {"name": "Okosóra", "price": "75000 Ft", "category": "Elektronika"}
    ]
    return render_template('add.html', products=products)

@app.route('/pizza-order', methods=["GET", "POST"])
def pizza_order():
    if request.method == "POST":
        _name = request.form.get("name")
        _phone = request.form.get("phone")
        _size = request.form.get("size")
        _toppings = request.form.get("toppings")
        _quantity = request.form.get("quantity")
        _deliverytime = request.form.get("deliverytime")
        _other = request.form.get("other")
        order ={
            "name": _name,
            "phone": _phone,
            "size": _size,
            "toppings": _toppings,
            "quantity": _quantity,
            "deliverytime": _deliverytime,
            "other":_other}
        orders.append(order)
        print(orders)
        return redirect(url_for('order_summary'))
    return render_template('pizza_order.html')

if __name__ == '__main__':
    app.run(debug=True)
