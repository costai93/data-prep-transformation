#########
INSERT INTO WideTableVendas (
    ano, mes, product_id, product_category_name, product_name_length, product_description_length, product_photos_qty, product_weight_g, product_length_cm, product_height_cm, product_width_cm,
    customer_id, customer_unique_id, customer_zip_code_prefix, customer_city, customer_state,
    seller_id, seller_zip_code_prefix, seller_city, seller_state,
    quantidade, valor_total
)
SELECT 
    YEAR(o.order_purchase_timestamp) AS ano,
    MONTH(o.order_purchase_timestamp) AS mes,
    p.product_id, p.product_category_name, p.product_name_length, p.product_description_length, p.product_photos_qty, p.product_weight_g, p.product_length_cm, p.product_height_cm, p.product_width_cm,
    c.customer_id, c.customer_unique_id, c.customer_zip_code_prefix, c.customer_city, c.customer_state,
    s.seller_id, s.seller_zip_code_prefix, s.seller_city, s.seller_state,
    oi.order_item_id AS quantidade, oi.price AS valor_total
FROM temp_olist_order_items_dataset oi
JOIN temp_olist_orders_dataset o ON oi.order_id = o.order_id
JOIN temp_olist_products_dataset p ON oi.product_id = p.product_id
JOIN temp_olist_customers_dataset c ON o.customer_id = c.customer_id
JOIN temp_olist_sellers_dataset s ON oi.seller_id = s.seller_id;
