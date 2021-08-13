import os
import numpy as np
import shutil
import random
import time
import subprocess
import json
import paho.mqtt.client as mqtt

sub_address = "/oneM2M/resp/antares-cse/c9ab16824dc3b3d4:c76af9ff466e3c4d/json"

def turnon_device(client):
    access_key = "c9ab16824dc3b3d4:c76af9ff466e3c4d"
    to = "/antares-cse/antares-id/e-eyes/sensor_state"
    topic = "/oneM2M/req/c9ab16824dc3b3d4:c76af9ff466e3c4d/antares-cse/json"

    content = {
            "m2m:rqp": {
                "fr": access_key,
                "to": to,
                "op": 1,
                "rqi": "turnon",
                "pc": {
                    "m2m:cin":{
                        "cnf": "message",
                        "con": 1
                    }
                },
                "ty": 4
            }
    }

    json_obj = json.dumps(content, indent = 1)
    client.publish(topic, json_obj)
    

def process_data_train():
    shutil.make_archive(dataset.zip, "zip", "dataset1/")

def main_process(state):
    if state == 0:
        #basic mode
        child = subprocess.Popen(['python', 'Face-Recognition.py'], stdin = subprocess.PIPE)
    elif state == 1:
        #train mode
        print("TRAIN MODE")
    elif state == 2:
        #train exec
        train_exec()

def process_message(message):
    mess_dict = json.loads(message)
    context = mess_dict["m2m:rsp"]["rqi"]
    content = mess_dict["m2m:rsp"]["pc"]["m2m:cin"]["con"]

    return context, content

def on_connect(client, userdata, flags, rc):
    print("Device connected with result code {}".format(str(rc)))

def on_message(client, userdata, message):
    context, content = process_message(message.payload.decode("utf-8"))

    if context == "turnon":
        print("Scanner starting")
        global child
        child = subprocess.Popen(["python", "Face-Recognition.py"], stdin=subprocess.PIPE)
    elif context == "server_trainSignal":
        child.communicate("q")

    elif context == "server_trainId":
        print("TEST")


broker = "mqtt.antares.id"
port = 1883
generate = random.randint(0, 100000)
client = mqtt.Client(str(generate))


client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, port)
client.subscribe(sub_address)

turnon_device(client)

client.loop_forever()
