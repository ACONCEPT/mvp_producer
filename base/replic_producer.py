#! usr/bin/env python3
from kafka import KafkaProducer
import sys
producer = KafkaProducer(bootstrap_servers=['localhost:9092','localhost:9093','localhost:9094'])
