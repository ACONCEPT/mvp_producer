#! usr/bin/env python3
import sys
sys.path.append("../base/")
from replic_consumer import consumer

def main():
    consumer("replicated_topic")


if __name__ == '__main__':
	main()
