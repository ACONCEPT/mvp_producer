#! usr/bin/env python3
from kafka import KafkaConsumer
#sudo $KAFKA/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic replicated_topic

def consumer(topic):
#    bootstrap_servers = ["localhost:9092"]
#    print("connecting to consumer with bootstrap servers {}".format(bootstrap_servers))
    consumer = KafkaConsumer(topic,\
                             group_id="python")
    while True:
        for message in consumer:
            print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                                  message.offset, message.key,
                                                  message.value))

if __name__ == "__main__":
    consumer("replicated_topic")
