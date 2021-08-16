#! c:\python34\python3
#!/usr/bin/env python
##demo code provided by Steve Cope at www.steves-internet-guide.com
##email steve@steves-internet-guide.com
##Free to use for any purpose
##If you like and use this code you can
##buy me a drink here https://www.paypal.me/StepenCope
""" Send File Using MQTT """
import time
import paho.mqtt.client as paho
import hashlib
#broker="broker.hivemq.com"
#broker="iot.eclipse.org"
broker="mqtt.antares.id"
filename="1DSCI0027.jpg"
#filename="chinese-proverb.jpg"
#filename="send-receive-file.7z"
topic="data/files"
qos=1
data_block_size=2000
file_out="copy-"+filename
fout=open(file_out,"wb") #use a different filename
# for outfile as I'm running sender and receiver together

def process_message(msg):
   """ This is the main receiver code
   """
   print("received ")
   global bytes_in
   if len(msg)==200: #is header or end
      print("found header")
      msg_in=msg.decode("utf-8")
      msg_in=msg_in.split(",,")
      if msg_in[0]=="end": #is it really last packet?
         in_hash_final=in_hash_md5.hexdigest()
         if in_hash_final==msg_in[2]:           
            print("File copied OK -valid hash  ",in_hash_final)
            return -1
         else:
            print("Bad file receive   ",in_hash_final)
         return False
      else:
         if msg_in[0]!="header":
            in_hash_md5.update(msg)
            return True
         else:
            return False
   else:
      bytes_in=bytes_in+len(msg)
      in_hash_md5.update(msg)
      print("found data bytes= ",bytes_in)
      return True
#define callback
def on_message(client, userdata, message):
   #time.sleep(1)
   global run_flag
   #print("received message =",str(message.payload.decode("utf-8")))
   ret=process_message(message.payload)
   if ret:
      fout.write(message.payload)
   if ret== -1:
      run_flag=False #exit receive loop
      print("complete file received")
   


bytes_in=0
client= paho.Client("client-receive-001")  #create client object client1.on_publish = on_publish                          #assign function to callback client1.connect(broker,port)                                 #establish connection client1.publish("data/files","on")  
######
client.on_message=on_message
client.mid_value=None
#####
print("connecting to broker ",broker)
client.connect(broker)#connect
#client.loop_start() #start loop to process received messages
print("subscribing ")
client.subscribe(topic)#subscribe
time.sleep(2)
start=time.time()
time_taken=time.time()-start
in_hash_md5 = hashlib.md5()
run_flag=True
while run_flag:
   client.loop(00.1)  #manual loop
   pass
client.disconnect() #disconnect
#client.loop_stop() #stop loop
fout.close()

