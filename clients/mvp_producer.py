#! usr/bin/env python3

import sys
sys.path.append("../base/")
import psycopg2
#from single_producer import producer
#from producer_menu import prompt_message, producer_menu
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
    data = get_mvp_data()[0]
    producer = KafkaProducer(bootstrap_servers=['54.218.31.15:9092'],value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    for record in data:
        future = producer.send("test",json.dumps(record))
        try:
            record_metadata = future.get(timeout=10)
            print(record_metadata)
        except KafkaError as e:
            print(e)

if __name__ == '__main__':
    send_to_test_topic()
