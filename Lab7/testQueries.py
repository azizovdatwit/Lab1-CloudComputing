# unittests.py

import unittest
import mysql.connector

class MyGuitarShopTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        try:
            cls.db = mysql.connector.connect(
                host="127.0.0.1",
                port=3307,  # change if needed
                user="root",
                password="Davud221#",
                database="my_guitar_shop"
            )
            cls.cursor = cls.db.cursor()
            print("Connected to database.")
        except mysql.connector.Error as err:
            print(f" Connection error: {err}")
            cls.db = None

    @classmethod
    def tearDownClass(cls):
        if cls.cursor:
            cls.cursor.close()
        if cls.db:
            cls.db.close()
            print("Connection closed.")

    def run_query(self, query):
        try:
            self.__class__.cursor.execute(query)
            return self.__class__.cursor.fetchall()
        except mysql.connector.Error as err:
            self.fail(f"Query failed: {err}")
            return None

    def test_query1(self):
        rows = self.run_query("SELECT zip_code FROM addresses LIMIT 5;")
        print("Query 1 results:", rows)
        self.assertIsNotNone(rows)

    def test_query2(self):
        rows = self.run_query("SELECT phone FROM addresses WHERE phone LIKE '2%';")
        print("Query 2 results:", rows)
        self.assertIsNotNone(rows)

    def test_query3(self):
        rows = self.run_query("SELECT category_id, COUNT(*) AS product_count FROM products GROUP BY category_id;")
        print("Query 3 results:", rows)
        self.assertTrue(rows and len(rows[0]) == 2)

    def test_query4(self):
        rows = self.run_query("SELECT YEAR(order_date) AS order_year, COUNT(*) AS total_orders FROM orders GROUP BY YEAR(order_date);")
        print("Query 4 results:", rows)
        self.assertIsNotNone(rows)

    def test_query5(self):
        rows = self.run_query("SELECT first_name, email_address FROM customers WHERE email_address LIKE 'a%';")
        print("Query 5 results:", rows)
        self.assertIsNotNone(rows)

    def test_query6(self):
        rows = self.run_query("SELECT city FROM addresses;")
        print("Query 6 results:", rows)
        self.assertIsNotNone(rows)

    def test_query7(self):
        rows = self.run_query("SELECT product_name FROM products WHERE list_price > 700;")
        self.assertIsNotNone(rows)

    def test_query8(self):
        rows = self.run_query("SELECT first_name FROM administrators;")
        self.assertIsNotNone(rows)

    def test_query9(self):
        rows = self.run_query("""
            SELECT o.order_id, oi.item_price, oi.quantity
            FROM order_items oi
            JOIN orders o ON oi.order_id = o.order_id;
        """)
        self.assertTrue(rows and len(rows[0]) == 3)

    def test_query10(self):
        rows = self.run_query("SELECT YEAR(order_date) AS order_year, COUNT(*) AS total_orders FROM orders GROUP BY YEAR(order_date);")
        self.assertIsNotNone(rows)

if __name__ == '__main__':
    unittest.main()
