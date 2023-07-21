import sqlite3
from sqlite3 import Error


def create_connection():
    conn = None
    try:
        conn = sqlite3.connect("sample.db")
        create_products_table(conn)
        create_product_sales_table(conn)
        return conn
    except Error as e:
        print(e)

    return conn


def check_connection():
    conn = create_connection()
    if conn is not None:
        return conn

    else:
        print("Error! cannot create the database connection.")


def execute_query(conn, query):
    try:
        c = conn.cursor()
        c.execute(query)
    except Error as e:
        print(e)


def create_products_table(conn):
    sql_create_product_table = """ CREATE TABLE IF NOT EXISTS products (
                                        id integer PRIMARY KEY,
                                        name integer Not NULL,
                                        price integer Not NULL
                                    ) """
    try:
        c = conn.cursor()
        c.execute(sql_create_product_table)
        conn.commit()
    except Error as e:
        print(e)


def create_product_sales_table(conn):
    sql_create_product_sales_table = """ CREATE TABLE IF NOT EXISTS order_history (
                                        id integer PRIMARY KEY,
                                        product_id integer NOT NULL,
                                        quantity integer Not NULL
                                    ) """
    try:
        c = conn.cursor()
        c.execute(sql_create_product_sales_table)
        conn.commit()
    except Error as e:
        print(e)


def create_product(name, price):
    insert_product = """INSERT INTO products(name, price) VALUES (?, ?)"""
    data = (name, price)
    conn = check_connection()
    try:
        c = conn.cursor()
        c.execute(insert_product, data)
        conn.commit()
        return "Data added successfully"
    except Error as e:
        print("error", e)


def update_product(name, price, id):
    update_product_name = """ UPDATE products SET name = ? WHERE id = ? """
    update_product_price = """ UPDATE products SET price = ? WHERE id = ? """
    conn = check_connection()
    try:
        c = conn.cursor()
        c.execute(update_product_name, (name, id))
        c.execute(update_product_price, (price, id))
        conn.commit()
        return "Updated successfully"
    except Error as e:
        print(e)


def delete_product(id):
    delete_product = """ DELETE from products WHERE id = ? """
    data = (id,)
    conn = check_connection()
    try:
        c = conn.cursor()
        c.execute(delete_product, data)
        conn.commit()
        return "Updated successfully"
    except Error as e:
        print(e)


def get_products():
    product_list = '''SELECT * from products'''
    conn = check_connection()
    try:
        c = conn.cursor()
        c.execute(product_list)
        result = c.fetchall()
        if len(result):
            keys = []
            values = []
            for i in c.description:
                for j in i:
                    if j:
                        keys.append(j)
            for j in result:
                values.append(dict(zip(keys, j)))
            return values
        else:
            return result
    except Error as e:
        print(e)


def get_product(id):
    get_product = '''SELECT * from products WHERE id = ?'''
    data = (id,)
    conn = check_connection()
    try:
        c = conn.cursor()
        c.execute(get_product, data)
        result = c.fetchone()
        if result:
            arr = []
            for i in c.description:
                for j in i:
                    if j:
                        arr.append(j)
            result = dict(zip(arr, result))
            return result
        else:
            return result
    except Error as e:
        print(e)


def create_order(product_id, quantity):
    insert_order = """INSERT INTO order_history(product_id, quantity) VALUES (?, ?)"""
    data = (product_id, quantity)
    conn = check_connection()
    try:
        c = conn.cursor()
        c.execute(insert_order, data)
        conn.commit()
        return "Data added successfully"
    except Error as e:
        print("error", e)


def get_order_history():
    order_history = '''SELECT * from order_history'''
    conn = check_connection()
    try:
        c = conn.cursor()
        c.execute(order_history)
        result = c.fetchall()
        if len(result):
            keys = []
            values = []
            for i in c.description:
                for j in i:
                    if j:
                        keys.append(j)
            for j in result:
                values.append(dict(zip(keys, j)))
            return values
        else:
            return result
    except Error as e:
        print(e)
