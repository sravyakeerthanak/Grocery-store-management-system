import mysql.connector

def get_sql_connection():
    return mysql.connector.connect(
        user='sravyakk',         # Ensure this is the correct username
        password='sravyakk',  # Ensure this is the correct password
        database='grocery_store'
    )
# import datetime
# import mysql.connector

# __cnx = None

# def get_sql_connection():
#   print("Opening mysql connection")
#   global __cnx

#   if __cnx is None:
#     __cnx = mysql.connector.connect(user='sravyakk', password='sravyakk', database='grocery_store')

#   return __cnx

