from sql_connection import get_sql_connection

def get_all_menuitems(connection):
    cursor = connection.cursor()
    query = "SELECT menu_item.menuitem_id, menu_item.resturant_id, menu_item.name, menu_item.description, menu_item.price, menu_item.image_url, menu_item.is_available FROM delivery.menu_item"
    cursor.execute(query)
    response = []

    for (menuitem_id, resturant_id, name, description, price, image_url, is_available) in cursor:
        response.append({
            "id": menuitem_id,
            "resturant_id": resturant_id,
            "name": name,
            "description": description,
            "price": price,
            "image_url": image_url,
            "is_available": is_available
        })
    return response

def get_resturant_menu_items(connection, resturant_id):
    cursor = connection.cursor()
    query = "SELECT menu_item.menuitem_id, menu_item.resturant_id, menu_item.name, menu_item.description, menu_item.price, menu_item.image_url, menu_item.is_available FROM delivery.menu_item WHERE menu_item.resturant_id="+str(resturant_id)
    cursor.execute(query)
    response = []

    for (menuitem_id, resturant_id, name, description, price, image_url, is_available) in cursor:
        response.append({
            "id": menuitem_id,
            "resturant_id": resturant_id,
            "name": name,
            "description": description,
            "price": price,
            "image_url": image_url,
            "is_available": is_available
        })
    return response

def add_menuitem(connection, item):
    cursor = connection.cursor()
    query = "INSERT INTO delivery.menu_item (resturant_id, name, description, price, image_url, is_available) VALUES (%s, %s, %s, %s, %s, %s)"
    data = (item['resturant_id'], item['itemName'], item['itemDescription'], item['itemPrice'], item['itemImageUrl'], item['itemIsAvailable'])
    cursor.execute(query, data)
    connection.commit()
    return cursor.lastrowid

def delete_menuitem(connection, item_id):
    cursor= connection.cursor()
    print(item_id)
    query = ("DELETE FROM delivery.menu_item WHERE menuitem_id ="+str(item_id))
    cursor.execute(query)
    connection.commit()
    return cursor.lastrowid

if __name__ == "__main__":
    connection = get_sql_connection()
    print(add_menuitem(connection, {
        "resturant_id": 1,
        "itemName": "paratha",
        "itemDescription": "i am paratha",
        "itemPrice": 200,
        "itemImageUrl": "image Url",
        "itemIsAvailable": 1
    }))
