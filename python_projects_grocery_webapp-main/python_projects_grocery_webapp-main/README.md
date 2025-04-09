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
