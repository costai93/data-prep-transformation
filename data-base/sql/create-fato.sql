-- Tabela de Dimensão: DimProduto
CREATE TABLE DimProduto (
    product_id VARCHAR(50) PRIMARY KEY,
    product_category_name VARCHAR(50),
    product_name_length INT,
    product_description_length INT,
    product_photos_qty INT,
    product_weight_g INT,
    product_length_cm INT,
    product_height_cm INT,
    product_width_cm INT
);

-- Tabela de Dimensão: DimCliente
CREATE TABLE DimCliente (
    customer_id VARCHAR(50) PRIMARY KEY,
    customer_unique_id VARCHAR(50),
    customer_zip_code_prefix INT,
    customer_city VARCHAR(50),
    customer_state VARCHAR(50)
);

-- Tabela de Dimensão: DimVendedor
CREATE TABLE DimVendedor (
    seller_id VARCHAR(50) PRIMARY KEY,
    seller_zip_code_prefix INT,
    seller_city VARCHAR(50),
    seller_state VARCHAR(50)
);

-- Tabela de Dimensão: DimTempo
CREATE TABLE DimTempo (
    tempo_id INT PRIMARY KEY AUTO_INCREMENT,
    ano INT,
    mes INT,
    dia INT
);

-- Tabela de Fato: FatoVendas
CREATE TABLE FatoVendas (
    venda_id INT PRIMARY KEY AUTO_INCREMENT,
    product_id VARCHAR(50),
    customer_id VARCHAR(50),
    seller_id VARCHAR(50),
    tempo_id INT,
    quantidade INT,
    valor_total DECIMAL(10, 2),
    FOREIGN KEY (product_id) REFERENCES DimProduto(product_id),
    FOREIGN KEY (customer_id) REFERENCES DimCliente(customer_id),
    FOREIGN KEY (seller_id) REFERENCES DimVendedor(seller_id),
    FOREIGN KEY (tempo_id) REFERENCES DimTempo(tempo_id)
);
