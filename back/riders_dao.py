from sql_connection import get_sql_connection

def get_all_riders(connection):
    cursor = connection.cursor()
    query = "SELECT rider.rider_id, rider.name, rider.phone, rider.vehicle_type, rider.current_location_lat, rider.current_location_lng, rider.is_available FROM delivery.rider"
    cursor.execute(query)
    response = []
    for (rider_id, name, phone, vehicle_type, lat, lng, is_available) in cursor:
        response.append({
            "rider_id": rider_id,
            "name": name,
            "phone": phone,
            "vehicle_type": vehicle_type,
            "current_location_lat": lat,
            "current_location_lng": lng,
            "is_available": is_available
        })
    return response

def insert_new_rider(connection, rider):
    cursor = connection.cursor()
    query = "INSERT INTO delivery.rider (name, phone, vehicle_type, current_location_lat, current_location_lng, is_available) VALUES (%s, %s, %s, %s, %s, %s)"
    data = (rider['name'], rider['phone'], rider['vehicle_type'], rider['current_location_lat'], rider['current_location_lng'], rider['is_available'])
    cursor.execute(query, data)
    connection.commit()
    return cursor.lastrowid 

def delete_rider(connection, rider_id):
    cursor = connection.cursor()
    query = "DELETE FROM delivery.rider WHERE rider_id = %s"
    cursor.execute(query, (rider_id,))
    connection.commit()
    return cursor.lastrowid

def get_rider_by_id(connection, rider_id):
    cursor = connection.cursor()
    query = "SELECT rider.rider_id, rider.name, rider.phone, rider.vehicle_type, rider.current_location_lat, rider.current_location_lng, rider.is_available FROM delivery.rider WHERE rider.rider_id = %s"
    cursor.execute(query, (rider_id,))
    response = cursor.fetchone()

    if response:
        return {
            "rider_id": response[0],
            "name": response[1],
            "email": response[2],
            "phone": response[3],
            "vehicle_type": response[4]
        }
    else:
        return None
    
if __name__ == "__main__":
    connection = get_sql_connection()
    print(get_rider_by_id(connection, 1))
