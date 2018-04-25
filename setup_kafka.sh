#! usr/bin/env bash
#Install java and zookeeper dependencies
sudo apt-get install default-jre
sudo apt-get install zookeeperd
cd ~/kafka
wget http://mirrors.ocf.berkeley.edu/apache/kafka/1.1.0/kafka_2.11-1.1.0.tgz
cd kafka_2.11-1.1.0
#start the zookeeper server
./bin/zookeeper-server-start.sh config/zookeeper.properties
# create a demo topic in the local kafka
# activate a console consumer on the topic demo
./bin/kafka-console-consumer.sh --topic demo --zookeeper localhost:2181
#install python 3 and create the venv for kafka
#sudo apt-get install -yq software-properties-common realpath python3.6 python3-pip xclip
#sudo apt-get install python3-venv
#cd ~/
#mkdir ~/envs
#cd envs
#python3 -m venv kafka
