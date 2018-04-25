#! usr/bin/env python3
import sys
sys.path.append("../base/")

def check_input(inpt):
    if inpt == "q":
        exit()

def prompt_message(msg = None, topic = None,options = None):
    thing = "{}\n".format(15 * "=")
    print(thing + "ENTER q TO EXIT AT ANY TIME\n" + thing)
    if not topic:
        topic = input("What topic are you sending to? ")
        check_input(topic)
    if not msg:
        msg = input("Please enter messasge content: ")
        check_input(msg)
    if options:
        if msg in options:
            return topic,group,msg
        else:
            return False
    return topic,msg

def producer_menu(producer,**kwargs):
    cont = True
    while cont:
        msg = prompt_message(**kwargs)
        if msg:
            topic = msg[0]
            msg = msg[1]
            print("received topic {} msg {} ".format(topic,msg))
            msg = msg.encode()
            print("msg encoded")
            producer.send(topic,msg)
            print("message sent")
        else:
            break
    return False

if __name__ == "__main__":
    producer_menu()
