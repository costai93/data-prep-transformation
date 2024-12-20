-- Tabela Wide Table: WideTableVendas
CREATE TABLE WideTableVendas (
    venda_id INT PRIMARY KEY AUTO_INCREMENT,
    ano INT,
    mes INT,
    product_id VARCHAR(50),
    product_category_name VARCHAR(50),
    product_name_length INT,
    product_description_length INT,
    product_photos_qty INT,
    product_weight_g INT,
    product_length_cm INT,
    product_height_cm INT,
    product_width_cm INT,
    customer_id VARCHAR(50),
    customer_unique_id VARCHAR(50),
    customer_zip_code_prefix INT,
    customer_city VARCHAR(50),
    customer_state VARCHAR(50),
    seller_id VARCHAR(50),
    seller_zip_code_prefix INT,
    seller_city VARCHAR(50),
    seller_state VARCHAR(50),
    quantidade INT,
    valor_total DECIMAL(10, 2)
);
