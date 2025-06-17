from sql_connection import get_sql_connection

def get_all_orders(connection):
    cursor = connection.cursor()
    query = "SELECT order.order_id, order.user_id, order.address_id, order.rider_id, order.resturant_id, order.total_price, order.status, order.created_at FROM delivery.order"
    cursor.execute(query)
    response = []

    for (order_id, user_id, address_id, rider_id, resturant_id, total_price, status, created_at) in cursor:
        response.append({
            "order_id": order_id,
            "user_id": user_id,
            "address_id": address_id,
            "rider_id": rider_id,
            "resturant_id": resturant_id,
            "total_price": total_price,
            "status": status,
            "created_at": created_at
        })
    return response

def get_order_by_id(connection, order_id):
    cursor = connection.cursor()
    query = "SELECT order.order_id, order.user_id, order.address_id, order.rider_id, order.resturant_id, order.total_price, order.status, order.created_at FROM delivery.order WHERE order.order_id = %s"
    cursor.execute(query, (order_id,))
    response = cursor.fetchone()

    if response:
        return {
            "order_id": response[0],
            "user_id": response[1],
            "address_id": response[2],
            "rider_id": response[3],
            "resturant_id": response[4],
            "total_price": response[5],
            "status": response[6],
            "created_at": response[7]
        }
    else:
        return None
    
def get_orders_by_user_id(connection, user_id):
    cursor = connection.cursor()
    query = "SELECT order.order_id, order.user_id, order.address_id, order.rider_id, order.resturant_id, order.total_price, order.status, order.created_at FROM delivery.order WHERE order.user_id = %s"
    cursor.execute(query, (user_id,))
    response = []

    for (order_id, user_id, address_id, rider_id, resturant_id, total_price, status, created_at) in cursor:
        response.append({
            "id": order_id,
            "user_id": user_id,
            "address_id": address_id,
            "rider_id": rider_id,
            "resturant_id": resturant_id,
            "total_price": total_price,
            "status": status,
            "created_at": created_at
        })
    return response

def get_orders_by_restaurant_id(connection, restaurant_id):
    cursor = connection.cursor()
    query = "SELECT order.order_id, order.user_id, order.address_id, order.rider_id, order.resturant_id, order.total_price, order.status, order.created_at FROM delivery.order WHERE order.resturant_id = %s"
    cursor.execute(query, (restaurant_id,))
    response = []

    for (order_id, user_id, address_id, rider_id, resturant_id, total_price, status, created_at) in cursor:
        response.append({
            "id": order_id,
            "user_id": user_id,
            "address_id": address_id,
            "rider_id": rider_id,
            "resturant_id": resturant_id,
            "total_price": total_price,
            "status": status,
            "created_at": created_at
        })
    
    return response

def get_orders_by_rider_id(connection, rider_id):
    cursor = connection.cursor()
    query = "SELECT order.order_id, order.user_id, order.address_id, order.rider_id, order.resturant_id, order.total_price, order.status, order.created_at FROM delivery.order WHERE order.rider_id = %s AND order.status= 'out-for-delivery'"
    cursor.execute(query, (rider_id,))
    response = []

    for (order_id, user_id, address_id, rider_id, resturant_id, total_price, status, created_at) in cursor:
        response.append({
            "id": order_id,
            "user_id": user_id,
            "address_id": address_id,
            "rider_id": rider_id,
            "resturant_id": resturant_id,
            "total_price": total_price,
            "status": status,
            "created_at": created_at
        })
    return response

def get_ready_orders(connection):
    cursor = connection.cursor()
    query = "SELECT order.order_id, order.user_id, order.address_id, order.rider_id, order.resturant_id, order.total_price, order.status, order.created_at FROM delivery.order WHERE order.status='ready'"
    cursor.execute(query)
    response = []

    for (order_id, user_id, address_id, rider_id, resturant_id, total_price, status, created_at) in cursor:
        response.append({
            "id": order_id,
            "user_id": user_id,
            "address_id": address_id,
            "rider_id": rider_id,
            "resturant_id": resturant_id,
            "total_price": total_price,
            "status": status,
            "created_at": created_at
        })
    return response

def create_order(connection, order_data):
    print(order_data)
    cursor = connection.cursor()
    query = "INSERT INTO delivery.order (user_id, address_id, resturant_id, total_price, status, created_at) VALUES (%s, %s, %s, %s, 'pending', NOW())"
    data = (
        order_data['user_id'],
        order_data['address_id'],
        order_data['resturant_id'],
        order_data['total_price']
    )
    cursor.execute(query, data)
    order_id = cursor.lastrowid
    print(order_id)

    details_query = "INSERT INTO delivery.order_details (oder_id, menuitem_id, quantity, unit_price) VALUES (%s,%s,%s,%s)"
    for item in order_data['items']:
        details_data = (
            order_id,
            item['menu_item_id'],
            item['quantity'],
            item['unit_price']
        )
        cursor.execute(details_query,details_data)

    connection.commit()
    return order_id


def update_order_status(connection, order_id, new_status):
    cursor = connection.cursor()
    query = "UPDATE delivery.order SET status = %s WHERE order_id = %s"
    cursor.execute(query, (new_status, order_id))
    connection.commit()
    return cursor.lastrowid

def assign_order_to_rider(connection, order_id, rider_data):
    print(rider_data['status'])
    cursor = connection.cursor()
    query = "UPDATE delivery.order SET rider_id = %s, status = %s WHERE order_id = %s"
    data = (
        rider_data['rider_id'],
        rider_data['status'],
        order_id
    )
    cursor.execute(query,data)
    connection.commit()
    return cursor.lastrowid

if __name__ == "__main__":
    connection = get_sql_connection()
    