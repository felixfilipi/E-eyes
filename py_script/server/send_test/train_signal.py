import sys
import time
import random
import json
import base64
import mysql.connector
import paho.mqtt.client as mqtt

broker = "mqtt.antares.id"
port = 1883
rqi = "try"
client = mqtt.Client(rqi)

access_key = "c9ab16824dc3b3d4:c76af9ff466e3c4d"
to = "/antares-cse/antares-id/e-eyes/send_file"
topic = "/oneM2M/req/c9ab16824dc3b3d4:c76af9ff466e3c4d/antares-cse/json"

# get user id
#state = sys.argv[1]

# convert file to base64
data = open("User.Felix Filipi.28.jpg", "rb").read()
encoded = base64.b64encode(data)
encoded_str = str(encoded)

content = {
    "m2m:rqp": {
        "fr": access_key,
        "to": to,
        "op": 1,
        "rqi": rqi,
        "pc": {
            "m2m:cin": {
                "cnf": "message",
                "con": encoded_str
            }
        },
        "ty": 4
    }
}

json_obj = json.dumps(content, indent = 1)


client.connect(broker, port)
client.publish(topic, json_obj)

print(str(1))
