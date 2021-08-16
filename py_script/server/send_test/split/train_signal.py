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
client.connect(broker, port)

# convert file to base64
data = open("User.Felix Filipi.28.jpg", "rb").read()
encoded = base64.b64encode(data)
encoded = encoded.decode("utf-8")

#encoded_bytes = encoded_string.encode("utf-8")
#decode_test = base64.b64decode(encoded_bytes)
#result = open("result.zip", "wb")
#result.write(decode_test)

print(len(encoded))
input("FASNL")

n = 100000
chunks = [encoded[i:i+n] for i in range(0, len(encoded), n)]

for i in range(len(chunks)):
    print(i)
    content = {
        "m2m:rqp": {
            "fr": access_key,
            "to": to,
            "op": 1,
            "rqi": rqi,
            "pc": {
                "m2m:cin": {
                    "cnf": "message",
                    "con": chunks[i]
                }
            },
            "ty": 4
        }
    }

    print(len(chunks[i]))

    json_obj = json.dumps(content, indent = 1)

    client.publish(topic, json_obj)
    time.sleep(2)
