import sqlite3 as sql

def insert_data(first_name,last_name,company,email,phone,street_address,city,state,country,zipcode):
    with sql.connect("app.db") as con:
        cur = con.cursor()
        cur.execute('INSERT INTO customer (first_name, last_name, company, email, phone) VALUES (?, ?, ?, ?, ?)', (first_name, last_name, company, email, phone))
        con.commit()
        customer_id = cur.execute('SELECT last_insert_rowid()').fetchall()[0][0]
        cur.execute('INSERT INTO address (street_address, city, state, country, zip_code, customer_customer_id) VALUES (?, ?, ?, ?, ?, ?)', (street_address,city,state,country,zipcode,customer_id))
        con.commit()


def insert_order(customer_id, name_of_part, manufacturer_of_part):
    with sql.connect("app.db") as con:
        cur = con.cursor()
        cur.execute('INSERT INTO `order` (name_of_part, manufacturer_of_part) VALUES (?, ?)', (name_of_part, manufacturer_of_part))
        con.commit()
        order_id = cur.execute('SELECT last_insert_rowid()').fetchall()[0][0]
        # insert into table order_has_customer
        cur.execute('INSERT INTO order_has_customer (order_order_id, customer_customer_id) VALUES (?, ?)', (order_id, customer_id))
        con.commit()

def retrieve_customers():
    with sql.connect("app.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        customers = cur.execute("select * from customer").fetchall()
        address = cur.execute("select * from address").fetchall()
    # calulate addresses for each customer
    numbers = []
    for customer in customers:
        count = 0
        for addr in address:
            if addr['customer_customer_id'] == customer['customer_id']:
                count += 1
        numbers.append(count)        
    return customers, address, numbers

def retrieve_orders():
    # confused about this part, I've referred to other people to figure out how this works
    with sql.connect('app.db') as con:
        orders = []
        con.row_factory = sql.Row
        cur = con.cursor()
        results = cur.execute('SELECT customer_customer_id FROM order_has_customer').fetchall()
        customer_ids = set( e['customer_customer_id'] for e in results )
        for id in customer_ids:
            tmp = {}
            customer_info = cur.execute('SELECT first_name, last_name from customer where customer_id=?', (int(id),)).fetchall()[0]
            tmp = {
                "first_name": customer_info['first_name'],
                "last_name": customer_info['last_name']
            }
            order_ids = cur.execute('SELECT order_order_id FROM order_has_customer WHERE customer_customer_id=?', (int(id),)).fetchall()
            tmp["orders"] = []
            for oid in order_ids:
                orders_tmp = cur.execute('SELECT name_of_part, manufacturer_of_part FROM `order` WHERE order_id=?', (int(oid['order_order_id']),)).fetchall()
                for ord in orders_tmp:
                    tmp["orders"].append({
                                        "name_of_part": ord['name_of_part'],
                                        "manufacturer_of_part": ord['manufacturer_of_part']
                                        })
            orders.append(tmp)
        return orders
