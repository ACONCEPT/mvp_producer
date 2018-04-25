#! usr/bin/env python3
from kafka import KafkaConsumer

def consumer(topic):
    bootstrap_servers = ["localhost:9092"]
    consumer = KafkaConsumer(topic,\
                             group_id="python",\
                             bootstrap_servers=bootstrap_servers)

    while True:
        for message in consumer:
            print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                                  message.offset, message.key,
                                                  message.value))
