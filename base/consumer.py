#! usr/bin/env python3
from kafka import KafkaConsumer

def main(topic,boostrap_servers = ["localhost:9092"]):

    consumer = KafkaConsumer(topic,\
                             group_id="python",\
                             bootstrap_servers=boostrap_servers)

    print("starting consumer for topic {} on servers {} ".format(topic,bootstrap_servers))
    while True:
        for message in consumer:
            print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                                  message.offset, message.key,
                                                  message.value))


if __name__ == "__main__":
    try:
        topic = sys.argv[1]
    except:
        topic = input("enter topic : ")
    try:
        bootstrap_servers = sys.argv[2]
    except:
        bootstrap_servers = int(input("enter number of bootstrap servers : "))
    main(topic,bootstrap_servers)
