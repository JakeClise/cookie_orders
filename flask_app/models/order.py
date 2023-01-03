from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Order:
    def __init__(self, data):
        self.id = data['id']
        self.customer_name = data['customer_name']
        self.cookie_type = data['cookie_type']
        self.number_of_boxes = data['number_of_boxes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @staticmethod
    def validate_order(order):
        is_valid = True
        if len(order['customer_name']) < 2:
            flash("Customer name must be at least two characters!")
            is_valid = False
        if len(order['cookie_type']) < 2:
            flash("Cookie type must be at least 2 characters!")
            is_valid = False
        if len(order['number_of_boxes']) < 1:
            flash("Must order at least one box of cookes for order to be valid!")
            is_valid = False
        return is_valid
        
        
    
    @classmethod
    def get_all_orders(cls):
        query = "SELECT * FROM orders;"
        results = connectToMySQL('cookie_orders').query_db(query)
        orders = []
        for order in results:
            orders.append(cls(order))
        return results
    
    @classmethod
    def save_order(cls, data):
        query = """INSERT INTO orders (customer_name, cookie_type, number_of_boxes) 
        VALUES (%(customer_name)s, %(cookie_type)s, %(number_of_boxes)s);
        """
        return connectToMySQL('cookie_orders').query_db(query, data)
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM orders WHERE id = %(id)s;"
        result = connectToMySQL('cookie_orders').query_db(query, data)
        return cls(result[0])

    @classmethod
    def edit_order(cls, data):
        query = """
        UPDATE orders SET customer_name = %(customer_name)s, cookie_type = %(cookie_type)s,
        number_of_boxes = %(number_of_boxes)s WHERE id = %(id)s;
        """
        return connectToMySQL('cookie_orders').query_db(query, data)


