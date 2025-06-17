from sql_connection import get_sql_connection

def get_all_users(connection):
    cursor = connection.cursor()
    query = "SELECT user.user_id, user.name, user.email, user.password, user.phone FROM delivery.User"
    cursor.execute(query)
    response = []

    for (user_id, name, email, password, phone) in cursor:
        response.append({
            "user_id": user_id,
            "name": name,
            "email": email,
            "password": password,
            "phone": phone
        })
    return response

def create_new_user(connection, user):
    cursor = connection.cursor()
    query = "INSERT INTO delivery.User (name, email, password, phone) VALUES (%s, %s, %s, %s)"
    data = (user['name'], user['email'], user['password'], user['phone'])
    cursor.execute(query, data)
    connection.commit()
    return cursor.lastrowid

def get_user_by_id(connection, user_id):
    cursor = connection.cursor()
    query = "SELECT user.user_id, user.name, user.email, user.password, user.phone FROM delivery.User WHERE user.user_id = %s"
    cursor.execute(query, (user_id,))
    response = cursor.fetchone()

    if response:
        return {
            "user_id": response[0],
            "name": response[1],
            "email": response[2],
            "password": response[3],
            "phone": response[4]
        }
    else:
        return None



if __name__ == "__main__":
    connection = get_sql_connection()
    print(get_all_users(connection))