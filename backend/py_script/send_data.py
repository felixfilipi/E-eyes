import sys
import time
import random
import json
import mysql.connector
import paho.mqtt.client as mqtt

broker = "mqtt.antares.id"
port = 1883
rqi = 1284
client = mqtt.Client(str(rqi))

access_key = "c9ab16824dc3b3d4:c76af9ff466e3c4d"
to = "/antares-cse/antares-id/e-eyes/train_signal"
topic = "/oneM2M/req/c9ab16824dc3b3d4:c76af9ff466e3c4d/antares-cse/json"

# connect to mysql
db = mysql.connector.connect(
    host = "localhost",
    user = "brian",
    password = "1234",
    database = "scanner"
)

# fetch data function
def sqlFetch(sql):
    cursor = db.cursor()
    cursor.execute(sql)
    return cursor.fetchall()

# return subject's name
def buildUser(data):
    firstname = data[0][1]
    lastname = data[0][2]
    name = firstname + " " + lastname
    userid = data[0][0]
    return userid, name

# get user id
user_id = sys.argv[1]

# get id data
query = "SELECT UserId, FirstName, LastName FROM UserData WHERE UserId = {}".format(user_id)

data = sqlFetch(query)
userid, name = buildUser(data)

signal = {
    "state": 1,
    "name": name
}
json_signal = json.dumps(signal, indent = 1)

content = {
    "m2m:rqp": {
        "fr": access_key,
        "to": to,
        "op": 1,
        "rqi": rqi,
        "pc": {
            "m2m:cin": {
                "cnf": "message",
                "con": str(signal)
            }
        },
        "ty": 4
    }
}

json_obj = json.dumps(content, indent = 1)


client.connect(broker, port)
client.publish(topic, json_obj)
