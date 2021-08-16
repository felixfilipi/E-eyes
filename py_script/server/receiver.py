import cv2
import os
import glob
import numpy as np
import random
import string
import time
import shutil
import datetime
import subprocess
import json
import base64
import paho.mqtt.client as mqtt
import mysql.connector
sub_address = "/oneM2M/resp/antares-cse/c9ab16824dc3b3d4:c76af9ff466e3c4d/json"
db = mysql.connector.connect(
    host = "localhost",
    user = "brian",
    password = "1234",
    database = "scanner"
)

def insert_user_photo(name):
    print(db)
    arr_val = glob.glob("../images/dataset/*" + name + "*")
    
    db_cursor = db.cursor()
    sql = "INSERT INTO UserPhoto VALUES (NULL, %s, %s)"

    arr_sql = []
    for i in range(len(arr_val)):
        split_str = arr_val[i].split("/", 3)
        name_files = split_str[3]
        tup = (name_files, "images/dataset/")
        arr_sql.append(tup)

    db_cursor.executemany(sql, arr_sql)
    db.commit()

    last_id = db_cursor.lastrowid
    return last_id

def user_id_search(name):
    name_arr = name.split()
    db_cursor = db.cursor(buffered = True)

    sql = "SELECT UserId FROM UserData WHERE FirstName = '{}'".format(name_arr[0]);

    db_cursor.execute(sql)
    result = db_cursor.fetchone()

    user_id = result[0]

    return user_id

def insert_user_dataset(first_id, user_id):
    photoid_arr = []
    for i in range(first_id, first_id + 30):
        photoid_arr.append(i)

    now = datetime.datetime.now()
    datetime_now = now.strftime("%Y-%m-%d %H:%M:%S")

    insert_arr = []
    for i in range(len(photoid_arr)):
        user_tuple = (user_id, photoid_arr[i], datetime_now)
        insert_arr.append(user_tuple)

    db_cursor = db.cursor()

    sql = "INSERT INTO UserDataset VALUES (%s, %s, %s)"

    db_cursor.executemany(sql, insert_arr)
    db.commit()
    
def database_process(name):
    first_id = insert_user_photo(name)
    user_id = user_id_search(name)
    print(first_id, user_id)
    insert_user_dataset(first_id, user_id)

def dataTrain_processing(b64_str):
    base64_bytes = b64_str.encode("utf-8")
    base64_decode = base64.b64decode(base64_bytes)
    result = open("archive.zip", "wb")
    result.write(base64_decode)

    #child = subprocess.Popen(["mv", "archive.zip", "../images/dataset/"])
    #child.wait()
    #time.sleep(2)

    shutil.unpack_archive("./archive.zip", "../images/dataset/")
    child = subprocess.Popen(["rm", "./archive.zip"])
    child.wait()

def scan_image_processing(b64):
    base64_bytes = b64.encode("utf-8")
    base64_decode = base64.b64decode(base64_bytes)
    result = open("scan/scan_image.jpg", "wb")
    result.write(base64_decode)

def image_predict():
    child = subprocess.Popen(['python', 'predict.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = child.communicate()
    out.decode("UTF-8").rstrip()
    out = str(out)
    str_split = out.split("'")
    out = str_split[1]
    str_split = out.split("\\")
    out = str_split[0]
    return out

def img_name_generator(size=10, chars=string.ascii_uppercase + string.digits):
   return ''.join(random.choice(chars) for _ in range(size))

def insert_scan_photo(userid):
    rand_string = img_name_generator()
    img_rename = "../images/data_scan/" + rand_string + ".jpg"
    child = subprocess.Popen(['mv', 'scan/scan_image.jpg', img_rename])
    child.wait()

    image_name = rand_string + ".jpg"
    
    db_cursor = db.cursor()
    sql = "INSERT INTO UserScanPhoto VALUES (NULL, %s, %s, %s)"

    val = (str(userid), image_name, "images/data_scan/")

    db_cursor.execute(sql, val)
    db.commit()


def get_data(name):
    name_arr = name.split()
    db_cursor = db.cursor()

    sql = "SELECT UserId, FirstName, LastName, Gender, Role FROM UserData WHERE FirstName = '{}'".format(name_arr[0])

    db_cursor.execute(sql)
    result = db_cursor.fetchone()

    userid = result[0]
    firstname = result[1]
    lastname = result[2]
    gender = result[3]
    role = result[4]

    return userid, firstname, lastname, gender, role

def insert_data_scan(userid, firstname, lastname, gender, role, temperature):
    now = datetime.datetime.now()
    datetime_now = now.strftime("%Y-%m-%d %H:%M:%S")
    db_cursor = db.cursor()

    sql = "INSERT INTO UserScan VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (str(userid), firstname, lastname, gender, role, datetime_now, str(temperature))

    db_cursor.execute(sql, val)
    db.commit()

def update_user_data(userid, temperature):
    now = datetime.datetime.now()
    datetime_now = now.strftime("%Y-%m-%d %H:%M:%S")
    db_cursor = db.cursor()

    sql = "UPDATE UserData SET LastScan = '{}', LastTemperature = '{}' WHERE UserId = '{}'".format(datetime_now, temperature, userid)
    db_cursor.execute(sql)

    db.commit()

def database_process_scan(name, temperature):
    userid, firstname, lastname, gender, role = get_data(name)
    insert_data_scan(userid, firstname, lastname, gender, role, temperature)
    update_user_data(userid, temperature)
    insert_scan_photo(userid)
    return name, role

def input_unknown_database(temperature):
    now = datetime.datetime.now()
    datetime_now = now.strftime("%Y-%m-%d %H:%M:%S")
    db_cursor = db.cursor()


def predict_send(name, role):
    access_key = "c9ab16824dc3b3d4:c76af9ff466e3c4d"
    to = "/antares-cse/antares-id/e-eyes/send_prediction"
    topic = "/oneM2M/req/c9ab16824dc3b3d4:c76af9ff466e3c4d/antares-cse/json"
    content = {
                "m2m:rqp": {
                    "fr": access_key,
                    "to": to,
                    "op": 1,
                    "rqi": "receive_predict",
                    "pc": {
                        "m2m:cin": {
                            "cnf": name,
                            "con": role
                    }
                },
                "ty": 4
            }
        }
    
    json_obj = json.dumps(content, indent = 1)
    client.publish(topic, json_obj)

def process_message(message):
    mess_dict = json.loads(message)
    context = mess_dict["m2m:rsp"]["rqi"]
    content = mess_dict["m2m:rsp"]["pc"]["m2m:cin"]["con"]
    cnf = mess_dict["m2m:rsp"]["pc"]["m2m:cin"]["cnf"]

    return context, content, cnf

#def message_length_extract(message):
#    mess_dict = json.loads(message)
#    name = mess_dict["name"]
#    encoded_length = mess_dict["length"]
#
#    return name, encoded_length

def on_connect(client, userdata, flags, rc):
    print("Server connected with result code {}".format(str(rc)))
    client.subscribe(sub_address)

def on_message(client, userdata, message):
    context, content, cnf = process_message(message.payload.decode("utf-8"))

    encoded_length = -1
    if context == "train_face":
        if content == "DONE":
            #name, encoded_length = message_length_extract(cnf)
            base64_raw = ''.join(new_arr)
            dataTrain_processing(base64_raw)
            database_process(cnf)
            child = subprocess.Popen(["python", "Train-Face.py"])
            child.wait()
        else:
            new_arr.append(content)
            #name, encoded_length = message_length_extract(cnf)
            #print("Send {} files from {}".format(len(new_arr), str(encoded_length)))
            print("{} file received".format(len(new_arr)))

        #if len(new_arr) == encoded_length:

    elif context == "face_detect":
        scan_image_processing(cnf)
        name = image_predict()
        print(name)

        if name == "Unknown":
            role = "Unknown"
            input_unknown_database(content)
        else:
            name, role = database_process_scan(name, content)
            
        predict_send(name, role)

broker = "mqtt.antares.id"
port = 1883
generate = random.randint(0, 100000)
client = mqtt.Client(str(generate))

global new_arr
new_arr = []
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, port)
client.loop_forever()
