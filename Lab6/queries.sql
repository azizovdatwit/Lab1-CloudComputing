select customer_id,address_id,line1 from my_guitar_shop.addresses;
select city from my_guitar_shop.addresses;
select product_name from my_guitar_shop.products WHERE list_price > 700; 
select product_name from my_guitar_shop.products WHERE list_price > 200 LIMIT 3; 
select email_address, first_name from my_guitar_shop.customers WHERE first_name like 'a%';
select Distinct state from my_guitar_shop.addresses WHERE city like 'L%';
select zip_code from my_guitar_shop.addresses LIMIT 5;
select phone from my_guitar_shop.addresses where phone like '2%';
select first_name from my_guitar_shop.administrators; 
select first_name, email_address from my_guitar_shop.customers where email_address like 'a%';

select Customers.first_name, Orders.order_id  from my_guitar_shop.orders INNER JOIN my_guitar_shop.customers ON Orders.customer_id = Customers.customer_id;
select Orders.ship_date, Order_items.order_id  from my_guitar_shop.order_items INNER JOIN my_guitar_shop.orders ON Order_items.order_id = Orders.order_id;
select Orders.order_id,Order_items.item_price, Order_items.quantity  from my_guitar_shop.order_items INNER JOIN my_guitar_shop.orders ON Order_items.order_id = Orders.order_id;
select Products.product_name, Products.list_price, Categories.category_name from my_guitar_shop.categories INNER JOIN my_guitar_shop.products ON Categories.category_id = Products.category_id;
select Customers.last_name, Orders.order_date  from my_guitar_shop.orders INNER JOIN my_guitar_shop.customers ON Orders.customer_id = Customers.customer_id;
select product_id, SUM(quantity) AS total_quantity_ordered from my_guitar_shop.order_items GROUP BY product_id;
select category_id, MAX(list_price) AS max_price from my_guitar_shop.products GROUP BY category_id;
select category_id, COUNT(*) AS product_count from my_guitar_shop.products GROUP BY category_id;
select YEAR(order_date) AS order_year, COUNT(*) AS total_orders from my_guitar_shop.orders GROUP BY YEAR(order_date);
select Addresses.state, COUNT(*) AS num_customers FROM my_guitar_shop.customers INNER JOIN my_guitar_shop.addresses ON Addresses.customer_id = Customers.customer_id GROUP BY Addresses.state;

