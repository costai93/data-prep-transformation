-- Tabela de Dimensão: DimProduto
INSERT INTO DimProduto (product_id, product_category_name, product_name_length, product_description_length, product_photos_qty, product_weight_g, product_length_cm, product_height_cm, product_width_cm)
SELECT DISTINCT product_id, product_category_name, product_name_length, product_description_length, product_photos_qty, product_weight_g, product_length_cm, product_height_cm, product_width_cm
FROM temp_olist_products_dataset;

-- Tabela de Dimensão: DimCliente
INSERT INTO DimCliente (customer_id, customer_unique_id, customer_zip_code_prefix, customer_city, customer_state)
SELECT DISTINCT customer_id, customer_unique_id, customer_zip_code_prefix, customer_city, customer_state
FROM temp_olist_customers_dataset;

-- Tabela de Dimensão: DimVendedor
INSERT INTO DimVendedor (seller_id, seller_zip_code_prefix, seller_city, seller_state)
SELECT DISTINCT seller_id, seller_zip_code_prefix, seller_city, seller_state
FROM temp_olist_sellers_dataset;

-- Tabela de Dimensão: DimTempo
INSERT INTO DimTempo (ano, mes, dia)
SELECT DISTINCT YEAR(order_purchase_timestamp) AS ano, MONTH(order_purchase_timestamp) AS mes, DAY(order_purchase_timestamp) AS dia
FROM temp_olist_orders_dataset;

-- Tabela de Fato: FatoVendas
INSERT INTO FatoVendas (product_id, customer_id, seller_id, tempo_id, quantidade, valor_total)
SELECT oi.product_id, o.customer_id, oi.seller_id, t.tempo_id, oi.order_item_id AS quantidade, oi.price AS valor_total
FROM temp_olist_order_items_dataset oi
JOIN temp_olist_orders_dataset o ON oi.order_id = o.order_id
JOIN DimTempo t ON t.ano = YEAR(o.order_purchase_timestamp) AND t.mes = MONTH(o.order_purchase_timestamp);
