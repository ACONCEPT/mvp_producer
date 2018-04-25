#! usr/bin/env bash

alias rlrc='source ~/.bashrc'
export KAFKA=$HOME'/kafkafiles/'
export ENVS=$HOME'/envs/'
export KAFKAENV=$ENVS'/kafka/'
export KAFKAACTIVATE=$KAFKAENV'/bin/activate'
export KAFKASRC=$KAFKAENV'/src/'
export KAFKAHOME=$HOME'/envs/'
export KAFKAENV=$HOME'/envs/kafka/bin/activate'
alias kafkaenv='source $KAFKAACTIVATE'
alias pytest='vim $KAFKASRC/test_kafka_connection.py'
alias kafkasrc='cd $KAFKASRC'
