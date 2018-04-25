#! usr/bin/env python3
import sys
sys.path.append("../base/")
from replic_producer import producer
from producer_menu import prompt_message, producer_menu

if __name__ == '__main__':
    producer_menu(producer,topic = "replicated_topic")
