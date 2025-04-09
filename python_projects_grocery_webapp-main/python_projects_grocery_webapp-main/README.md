# python_projects_grocery_webapp
In this python project, we will build a grocery store management application. It will be 3 tier application,
1. Front end: UI is written in HTML/CSS/Javascript/Bootstrap
2. Backend: Python and Flask
3. Database: mysql

![](homepage.JPG)

### Installation Instructions

Download mysql for windows: https://dev.mysql.com/downloads/installer/

`pip install mysql-connector-python`

----------------------------- Step 1: Create the `uom` table-----------------------------
CREATE TABLE grocery_store.uom (
    uom_id INT NOT NULL AUTO_INCREMENT,
    uom_name VARCHAR(45) NOT NULL,
    PRIMARY KEY (uom_id)
);

------------------------------- Step 2: Create the `products` table without a foreign key-----------------------------
CREATE TABLE grocery_store.products (
    product_id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    uom_id INT NOT NULL,
    price_per_unit DOUBLE NOT NULL,
    PRIMARY KEY (product_id)
);

------------------------------- Step 3: Insert data into the `uom` table-----------------------------
INSERT INTO grocery_store.uom (uom_name)
VALUES ('Piece'), ('Kilogram'), ('Liter');

-- Step 4: Insert data into `products` table (using the correct `uom_id` values)
INSERT INTO grocery_store.products (name, uom_id, price_per_unit)
VALUES ('Toothpaste', 1, 30); -- Assuming 'Piece' has uom_id = 1

------------------------------- Step 5: Add the foreign key constraint to `products` table-----------------------------
ALTER TABLE grocery_store.products
ADD CONSTRAINT fk_uom_id
FOREIGN KEY (uom_id)
REFERENCES grocery_store.uom(uom_id)
ON DELETE NO ACTION;

-- Step 6: Create the `orders` table
CREATE TABLE grocery_store.orders (
    order_id INT NOT NULL AUTO_INCREMENT,
    customer_name VARCHAR(100) NOT NULL,
    total DOUBLE NOT NULL,
    datetime DATETIME NOT NULL,
    PRIMARY KEY (order_id)
);

----------------------------- Step 7: Create the `order_details` table with foreign keys--------------------------------------
CREATE TABLE grocery_store.order_details (
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity DOUBLE NOT NULL,
    total_price DOUBLE NOT NULL,
    PRIMARY KEY (order_id, product_id), -- Composite primary key
    INDEX fk_product_id_idx (product_id ASC) VISIBLE,
    CONSTRAINT fk_order_id
        FOREIGN KEY (order_id)
        REFERENCES grocery_store.orders (order_id)
        ON DELETE NO ACTION
        ON UPDATE RESTRICT,
    CONSTRAINT fk_product_id
        FOREIGN KEY (product_id)
        REFERENCES grocery_store.products (product_id)
        ON DELETE NO ACTION
        ON UPDATE RESTRICT
);
------------------------------------------------------------------------------------------------------------------------------

MySQL> CREATE USER 'sravyakk'@'localhost' IDENTIFIED BY 'sravyakk';
Query OK, 0 rows affected (0.02 sec)

mysql> GRANT ALL PRIVILEGES ON grocery_store.* TO 'sravyakk'@'localhost';
Query OK, 0 rows affected (0.01 sec)

MySQL> FLUSH PRIVILEGES;
Query OK, 0 rows affected (0.01 sec)

MySQL> FLUSH PRIVILEGES;
Query OK, 0 rows affected (0.01 sec)

mysql> use grocery_store;
Database changed
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| grocery_store      |
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.01 sec)

mysql> use grocery_store;
Database changed
mysql> show tables;
+-------------------------+
| Tables_in_grocery_store |
+-------------------------+
| order_details           |
| orders                  |
| products                |
| uom                     |
+-------------------------+
4 rows in set (0.00 sec)

mysql> select * from uom;
+--------+----------+
| uom_id | uom_name |
+--------+----------+
|      1 | Piece    |
|      2 | Kilogram |
|      3 | Liter    |
+--------+----------+
3 rows in set (0.00 sec)

mysql> select * from products;
+------------+----------------+--------+----------------+
| product_id | name           | uom_id | price_per_unit |
+------------+----------------+--------+----------------+
|          3 | OIL            |      3 |            100 |
|          4 | pastry         |      1 |            130 |
|          5 | Colgate        |      1 |             70 |
|          6 | water          |      3 |             40 |
|          7 | Cookies        |      1 |             50 |
|          8 | Meat           |      2 |            200 |
|          9 |  garam masala  |      2 |            150 |
+------------+----------------+--------+----------------+
7 rows in set (0.00 sec)

mysql> select * from orders;
+----------+---------------+-------+---------------------+
| order_id | customer_name | total | datetime            |
+----------+---------------+-------+---------------------+
|        1 | sravya        |   580 | 2024-09-04 15:30:08 |
|        2 | cleo          |   200 | 2024-09-04 15:30:23 |
|        3 | mylo          |   400 | 2024-09-04 15:30:45 |
|        4 | Julie         |   400 | 2024-09-04 15:31:11 |
|        5 | Dora          |   240 | 2024-09-04 15:31:29 |
+----------+---------------+-------+---------------------+
5 rows in set (0.00 sec)

mysql> select * from order_details;
+----------+------------+----------+-------------+
| order_id | product_id | quantity | total_price |
+----------+------------+----------+-------------+
|        1 |          4 |        2 |         260 |
|        1 |          5 |        1 |          70 |
|        1 |          7 |        5 |         250 |
|        2 |          8 |        1 |         200 |
|        3 |          8 |        2 |         400 |
|        4 |          8 |        2 |         400 |
|        5 |          6 |        1 |          40 |
|        5 |          8 |        1 |         200 |
+----------+------------+----------+-------------+
8 rows in set (0.00 sec)