from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.order import Order


@app.route('/cookies')
def cookies_home():
    orders = Order.get_all_orders()
    return render_template('cookies.html', orders = orders)

@app.route('/go-create-new-order')
def go_create_order():
    return render_template('new_order.html')

@app.route('/create-new-order', methods = ["POST"])
def create_order():
    if not Order.validate_order(request.form):
        return render_template('/new_order.html')
    Order.save_order(request.form)
    return redirect('/cookies')

@app.route('/go-edit-order/<int:id>')
def go_edit_order(id):
    data = {
        "id":id
    }
    return render_template('edit_order.html', order = Order.get_one(data))

@app.route('/edit-order', methods = ["POST"])
def edit_order():
    Order.edit_order(request.form)
    return redirect('/cookies')