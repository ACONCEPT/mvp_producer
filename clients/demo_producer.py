#! usr/bin/env python3
import sys
sys.path.append("../base/")
import psycopg2
from single_producer import producer
from producer_menu import prompt_message, producer_menu
from postgres_cursor import  get_cursor, execute_query,close_cursor

def get_mvp_data():
    query = "select * from parts limit 1;"
    data = execute_query(qery)
    return data


if __name__ == '__main__':
    print(get_mvp_data)
#    producer_menu(producer,topic = "demo")
