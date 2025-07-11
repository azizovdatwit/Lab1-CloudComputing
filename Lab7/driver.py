import mysql.connector
def driver():
    sqlQueries = {
        "1": "select zip_code from my_guitar_shop.addresses LIMIT 5;",
        "2": "select phone from my_guitar_shop.addresses where phone like '2%';",
        "3": "select category_id, COUNT(*) AS product_count from my_guitar_shop.products GROUP BY category_id;",
        "4": "select YEAR(order_date) AS order_year, COUNT(*) AS total_orders from my_guitar_shop.orders GROUP BY YEAR(order_date);",
        "5": "select first_name, email_address from my_guitar_shop.customers where email_address like 'a%';",
        "6": "select city from my_guitar_shop.addresses;",
        "7": "select product_name from my_guitar_shop.products WHERE list_price > 700;",
        "8": "select first_name from my_guitar_shop.administrators;",
        "9": "select Orders.order_id,Order_items.item_price, Order_items.quantity  from my_guitar_shop.order_items INNER JOIN my_guitar_shop.orders ON Order_items.order_id = Orders.order_id;",
        "10": "select YEAR(order_date) AS order_year, COUNT(*) AS total_orders from my_guitar_shop.orders GROUP BY YEAR(order_date);"
    }

    continueLoop = True
    while(continueLoop):
        for key, value in sqlQueries.items():
            print(f"{key}: {value}")
        print("0, Exit");

        choice = input("Enter your choice (0-10): ")
        if choice == "0":
            continueLoop = False
        else:
            print("userinput sql queries: \n", sqlQueries.get(choice))
            mydb = connect_to_db()
            query_addresses(mydb, sqlQueries[choice])

def connect_to_db():
    try:
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            port=3307,
            user="root",
            password="Davud221#",
            database="my_guitar_shop"
        )
        print("Successfully connected to MySQL database!")

    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")

    return mydb

def query_addresses(mydb, qry):
    try:
        # Establish a connection to the MySQL database
        if mydb == None:
            print("reconnection to db required")
            mydb = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="",
                database="my_guitar_shop"
            )

        # Create a cursor object to execute SQL queries
        mycursor = mydb.cursor()

        # Define the SQL SELECT query
        sql_query = qry

        # Execute the query
        mycursor.execute(sql_query)

        # Fetch all the results
        # Use fetchone() to retrieve a single row, or fetchmany(size) for a specific number of rows
        results = mycursor.fetchall()

        # Iterate through the fetched results and print them
        for row in results:
            print(row)

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close the cursor and the database connection
        if mydb.is_connected():
            mydb.close()
        print("MySQL connection closed.")

if __name__ == "__main__":
    driver()