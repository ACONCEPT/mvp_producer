import psycopg2
from kafka import KafkaProducer
from postgres_cursor import  get_cursor, execute_query,close_cursor
import json
import os

def get_mvp_data():
    get_cursor()
    query = "select * from sales_orders limit 5;"
    data = execute_query(query)
    close_cursor()
    return data

def json_serializer(v):
    return 

def send_to_test_topic(bootstrap_servers):
    data, header = get_mvp_data()
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers,\
                             value_serializer=lambda v: json.dumps(v).encode("utf-8"))

    for record in data:
        print("=" * 50)
        print(" "*20 + "NEW SQL RECORD")
        print("=" * 50)
        record = {str(h.name):str(v) for h,v in zip(header,record)}
        for key, val in record.items():
            print("COlUMN : {} ".format(key))
            print("VALUE ; {} ".format(val))
        record["table"] = "parts"
        future = producer.send("test",json.dumps(record))
        try:
            record_metadata = future.get(timeout=10)
        except KafkaError as e:
            print(e)

if __name__ == '__main__':
    fn = os.environ.get("HOME") +"/clusterinfo"
    with open(fn ,"r") as f:
        bootstrap_servers = ["{}:9092".format(x) for x in f.readlines()]
    send_to_test_topic(bootstrap_servers)
