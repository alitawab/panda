from flask import Flask, request, jsonify
from sql_connection import get_sql_connection
import menuitems_dao
import users_dao
import resturants_dao
import orders_dao

app = Flask(__name__)
connection = get_sql_connection()

@app.route('/getMenuItems', methods=['GET'])
def getMenuItems():
    menu_items = menuitems_dao.get_all_menuitems(connection)
    response = jsonify(menu_items)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getResturantMenu/<int:resturant_id>', methods=['GET'])
def getResturantMenu(resturant_id):
    menu_items = menuitems_dao.get_resturant_menu_items(connection,resturant_id)
    response = jsonify(menu_items)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/addMenuItems', methods=['POST'])
def addMenuItems():
    request_payload = request.get_json()
    item_id = menuitems_dao.add_menuitem(connection, request_payload)
    response = jsonify({"item_id":item_id})
    response.headers.add('Access-Contorl-Allow-Origin','*')
    return response

@app.route('/deleteMenuItems/<int:item_id>', methods=['DELETE'])
def deleteMenuItem(item_id):
    return_id = menuitems_dao.delete_menuitem(connection,item_id)
    return jsonify({"deleted_id": return_id})


@app.route('/createOrder', methods=['POST'])
def createOrder():
    request_payload = request.get_json()
    item_id = orders_dao.create_order(connection, request_payload)
    response = jsonify({"item_id":item_id})
    response.headers.add('Access-Contorl-Allow-Origin','*')
    return response


@app.route('/getAllOrders', methods=['GET'])
def getAllOrders():
    orders = orders_dao.get_all_orders(connection)
    response = jsonify(orders)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getOrderByResturant/<int:resturant_id>', methods=['GET'])
def getResturantOrder(resturant_id):
    orders = orders_dao.get_orders_by_restaurant_id(connection,resturant_id)
    response = jsonify(orders)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getOrderByUser/<int:user_id>', methods=['GET'])
def getUserOrder(user_id):
    orders = orders_dao.get_orders_by_user_id(connection,user_id)
    response = jsonify(orders)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/updateOrderStatus/<int:order_id>/<status>', methods=['PUT'])
def updateOrderStatus(order_id,status):
    return_id = orders_dao.update_order_status(connection, order_id, status)
    return jsonify({"update_id": return_id})

@app.route('/getReadyOrder' , methods=['GET'])
def getReadyOrder():
    readyOrders = orders_dao.get_ready_orders(connection)
    response = jsonify(readyOrders)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/assignOrderToRider/<int:order_id>', methods=['PUT'])
def assignOrderToRider(order_id):
    request_payload = request.get_json()
    return_id = orders_dao.assign_order_to_rider(connection,order_id,request_payload)
    return jsonify({"assign_id": return_id})

@app.route('/getRiderDelivery/<int:rider_id>', methods=['GET'])
def getRiderDelivery(rider_id):
    riderDeliveries = orders_dao.get_orders_by_rider_id(connection, rider_id)
    response = jsonify(riderDeliveries)
    response.headers.add('Access-Control-Allow-Origin' , '*')
    return response

@app.route('/getUser', methods=['GET'])
def getUser():
    user = users_dao.get_all_users(connection)
    response = jsonify(user)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getResturant', methods=['GET'])
def getResturant():
    restaurant = resturants_dao.get_all_resturants(connection)
    response = jsonify(restaurant)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response



if __name__ == '__main__':
    print("Starting server...")
    app.run(host='0.0.0.0' , port=5000)