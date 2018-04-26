import psycopg2
from kafka import KafkaProducer
from postgres_cursor import  get_cursor, execute_query,close_cursor
import json

def get_mvp_data():
    get_cursor()
    query = "select * from parts limit 5;"
    data = execute_query(query)
    close_cursor()
    return data

def send_to_test_topic():
    data, header = get_mvp_data()
    producer = KafkaProducer(bootstrap_servers=['54.218.31.15:9092'],value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    for record in data:
        record = {str(h.name):str(v) for h,v in zip(header,record)}
        record["table"] = "parts"
        future = producer.send("test",json.dumps(record))
        try:
            record_metadata = future.get(timeout=10)
            print(record_metadata)
        except KafkaError as e:
            print(e)

if __name__ == '__main__':
    send_to_test_topic()
