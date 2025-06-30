from flask import Flask, request, jsonify
from flask_cors import CORS
from kafka import KafkaProducer
import json

app = Flask(__name__)
CORS(app) 
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

@app.route('/interest', methods=['POST'])
def track_interest():
    data = request.json
    producer.send('user_interest', value=data)
    producer.flush()
    return jsonify({"status": "success", "data": data})

if __name__ == '__main__':
    app.run(port=5000)
