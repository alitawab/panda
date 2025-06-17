import mysql.connector

__cxn = None

def get_sql_connection():
    print("Connecting to SQL database...")
    global __cxn

    if __cxn is None:
        __cxn = mysql.connector.connect(host='127.0.0.1',
                                        user='root',
                                        password='12345678',
                                        database='delivery')
    return __cxn