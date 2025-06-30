from kafka import KafkaConsumer
import mysql.connector
import json

# MySQL setup
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Password123',   # ← replace with your MySQL root password
    database='ecommerce'
)
cursor = conn.cursor()

# Kafka setup
consumer = KafkaConsumer(
    'user_interest',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("🟢 Listening for user interest events...")

for message in consumer:
    data = message.value
    print("➡️ Received:", data)
    cursor.execute(
        "INSERT INTO user_interest (user_id,user_name, product) VALUES (%s, %s,%s)",
        (data['user_id'], data['user_name'],data['product'])
    )
    conn.commit()
