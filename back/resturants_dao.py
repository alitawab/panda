from sql_connection import get_sql_connection

def get_all_resturants(connection):
    cursor = connection.cursor()
    query = "SELECT resturant.resturant_id, resturant.name, resturant.address, resturant.logo_url, resturant.phone, resturant.rating, resturant.open_hours FROM delivery.resturant"
    cursor.execute(query)
    response = []

    for (resturant_id, name, address, logo_url, phone, rating, open_hours) in cursor:
        response.append({
            "id": resturant_id,
            "name": name,
            "address": address,
            "logo_url": logo_url,
            "phone": phone,
            "rating": rating,
            "open_hours": open_hours
        })
    return response

def insert_new_resturant(connection, resturant):
    cursor = connection.cursor()
    query = "INSERT INTO delivery.resturant (name, address, logo_url, phone, rating, open_hours) VALUES (%s, %s, %s, %s, %s, %s)"
    data = (resturant['name'], resturant['address'], resturant['logo_url'], resturant['phone'], resturant['rating'], resturant['open_hours'])
    cursor.execute(query, data)
    connection.commit()
    return cursor.lastrowid

def delete_resturant(connection, resturant_id):
    cursor = connection.cursor()
    query = "DELETE FROM delivery.resturant WHERE resturant_id = %s"
    cursor.execute(query, (resturant_id,))
    connection.commit()
    return cursor.lastrowid

if __name__ == "__main__":
    connection = get_sql_connection()
    print(get_all_resturants(connection))
