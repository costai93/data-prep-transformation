#####
import pandas as pd
import mysql.connector

# Conexão com o banco de dados
conn = mysql.connector.connect(
    host='localhost',
    user='seu_usuario',
    password='sua_senha',
    database='seu_banco_de_dados'
)
cursor = conn.cursor()

# Função para carregar dados para uma tabela temporária
def load_data_from_csv_to_temp_table(table_name, csv_file, columns):
    df = pd.read_csv(csv_file)
    for index, row in df.iterrows():
        cursor.execute(f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(['%s'] * len(columns))})",
                       tuple(row[col] for col in columns))
    conn.commit()

# Carregar dados para as tabelas temporárias
load_data_from_csv_to_temp_table(
    'temp_olist_order_reviews_dataset',
    'olist_order_reviews_dataset.csv',
    ['review_id', 'order_id', 'review_score', 'review_comment_title', 'review_comment_message', 'review_creation_date', 'review_answer_timestamp']
)
load_data_from_csv_to_temp_table(
    'temp_olist_orders_dataset',
    'olist_orders_dataset.csv',
    ['order_id', 'customer_id', 'order_status', 'order_purchase_timestamp', 'order_approved_at', 'order_delivered_carrier_date', 'order_delivered_customer_date', 'order_estimated_delivery_date']
)
# Adicione outras tabelas conforme necessário

# Fechar a conexão com o banco de dados
cursor.close()
conn.close()

######
# Tabela de Dimensão: DimProduto
INSERT INTO DimProduto (product_id, product_category_name, product_name_length, product_description_length, product_photos_qty, product_weight_g, product_length_cm, product_height_cm, product_width_cm)
SELECT DISTINCT product_id, product_category_name, product_name_length, product_description_length, product_photos_qty, product_weight_g, product_length_cm, product_height_cm, product_width_cm
FROM temp_olist_products_dataset;

# Tabela de Dimensão: DimCliente
INSERT INTO DimCliente (customer_id, customer_unique_id, customer_zip_code_prefix, customer_city, customer_state)
SELECT DISTINCT customer_id, customer_unique_id, customer_zip_code_prefix, customer_city, customer_state
FROM temp_olist_customers_dataset;

# Tabela de Dimensão: DimVendedor
INSERT INTO DimVendedor (seller_id, seller_zip_code_prefix, seller_city, seller_state)
SELECT DISTINCT seller_id, seller_zip_code_prefix, seller_city, seller_state
FROM temp_olist_sellers_dataset;

# Tabela de Dimensão: DimTempo
INSERT INTO DimTempo (ano, mes, dia)
SELECT DISTINCT YEAR(order_purchase_timestamp) AS ano, MONTH(order_purchase_timestamp) AS mes, DAY(order_purchase_timestamp) AS dia
FROM temp_olist_orders_dataset;

# Tabela de Fato: FatoVendas
INSERT INTO FatoVendas (product_id, customer_id, seller_id, tempo_id, quantidade, valor_total)
SELECT oi.product_id, o.customer_id, oi.seller_id, t.tempo_id, oi.order_item_id AS quantidade, oi.price AS valor_total
FROM temp_olist_order_items_dataset oi
JOIN temp_olist_orders_dataset o ON oi.order_id = o.order_id
JOIN DimTempo t ON t.ano = YEAR(o.order_purchase_timestamp) AND t.mes = MONTH(o.order_purchase_timestamp);
