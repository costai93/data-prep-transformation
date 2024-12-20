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

# Fechar a conexão com o banco de dados
cursor.close()
conn.close()
