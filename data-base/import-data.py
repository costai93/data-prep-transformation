#pip install pandas mysql-connector-python
import pandas as pd
import mysql.connector

# Configurar a conexão com o banco de dados
conn = mysql.connector.connect(
    host='localhost',
    user='seu_usuario',
    password='sua_senha',
    database='seu_banco_de_dados'
)
cursor = conn.cursor()

# Função para carregar dados para uma tabela
def load_data_from_csv_to_db(table_name, csv_file, columns):
    df = pd.read_csv(csv_file)
    for index, row in df.iterrows():
        cursor.execute(f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(['%s'] * len(columns))})",
                       tuple(row[col] for col in columns))
    conn.commit()

# Carregar dados para a tabela olist_order_reviews_dataset
load_data_from_csv_to_db(
    'olist_order_reviews_dataset',
    'olist_order_reviews_dataset.csv',
    ['review_id', 'order_id', 'review_score', 'review_comment_title', 'review_comment_message', 'review_creation_date', 'review_answer_timestamp']
)

# Carregar dados para a tabela olist_orders_dataset
load_data_from_csv_to_db(
    'olist_orders_dataset',
    'olist_orders_dataset.csv',
    ['order_id', 'customer_id', 'order_status', 'order_purchase_timestamp', 'order_approved_at', 'order_delivered_carrier_date', 'order_delivered_customer_date', 'order_estimated_delivery_date']
)

# Carregar dados para a tabela olist_products_dataset
load_data_from_csv_to_db(
    'olist_products_dataset',
    'olist_products_dataset.csv',
    ['product_id', 'product_category_name', 'product_name_lenght', 'product_description_lenght', 'product_photos_qty', 'product_weight_g', 'product_length_cm', 'product_height_cm', 'product_width_cm']
)

# Carregar dados para a tabela olist_sellers_dataset
load_data_from_csv_to_db(
    'olist_sellers_dataset',
    'olist_sellers_dataset.csv',
    ['seller_id', 'seller_zip_code_prefix', 'seller_city', 'seller_state']
)

# Carregar dados para a tabela product_category_name_translation
load_data_from_csv_to_db(
    'product_category_name_translation',
    'product_category_name_translation.csv',
    ['product_category_name', 'product_category_name_english']
)

# Carregar dados para a tabela olist_customers_dataset
load_data_from_csv_to_db(
    'olist_customers_dataset',
    'olist_customers_dataset.csv',
    ['customer_id', 'customer_unique_id', 'customer_zip_code_prefix', 'customer_city', 'customer_state']
)

# Carregar dados para a tabela olist_geolocation_dataset
load_data_from_csv_to_db(
    'olist_geolocation_dataset',
    'olist_geolocation_dataset.csv',
    ['geolocation_zip_code_prefix', 'geolocation_lat', 'geolocation_lng', 'geolocation_city', 'geolocation_state']
)

# Carregar dados para a tabela olist_order_items_dataset
load_data_from_csv_to_db(
    'olist_order_items_dataset',
    'olist_order_items_dataset.csv',
    ['order_id', 'order_item_id', 'product_id', 'seller_id', 'shipping_limit_date', 'price', 'freight_value']
)

# Carregar dados para a tabela olist_order_payments_dataset
load_data_from_csv_to_db(
    'olist_order_payments_dataset',
    'olist_order_payments_dataset.csv',
    ['order_id', 'payment_sequential', 'payment_type', 'payment_installments', 'payment_value']
)

# Fechar a conexão com o banco de dados
cursor.close()
conn.close()
