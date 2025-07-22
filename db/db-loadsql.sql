--Creating Cafe Database called 'cafe'

CREATE DATABASE cafe; 

--Creating Products Table in Cafe Database called 'products'

CREATE TABLE 'products' (
    'Id' int(11) AUTO_INCREMENT NOT NULL,
    'Product_Name' varchar(250) NOT NULL,
    'Product_Price' float NOT NULL,
    'Purchase_Date' date NOT NULL,
        PRIMARY KEY ('Id')
    );

--Loading Data for Table 'products'

INSERT INTO 'products' ('Product_Name','Product_Price','Purchase_Date') VALUES
('Latte', 3.99, '2024-01-2'),
('Tea', 2.00, '2024-01-10'),
('Chocolate Cake', 4.50, '2024-01-11'),
('Carrot Cake', 3.50, '2024-01-15'),
('Cheese Cake', 5.00, '2024-01-15');
