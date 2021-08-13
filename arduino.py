import time
import RPi.GPIO as GPIO
import mlx90614
from smbus2 import SMBus

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO_BUZZER = 17
GPIO_TRIGGER = 23
GPIO_ECHO = 24
GPIO.setup(GPIO_BUZZER, GPIO.OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

GPIO.output(GPIO_TRIGGER, GPIO.LOW)
GPIO.output(GPIO_BUZZER, GPIO.LOW)

def get_range():
    GPIO.output(GPIO_TRIGGER, True)
    #time.sleep(0.001)

    GPIO.output(GPIO_TRIGGER, False)
    timeout_counter = int(time.time())
    start = time.time()

    while GPIO.input(GPIO_ECHO)==0 and (int(time.time())-timeout_counter) < 3:
        start = time.time()

    timeout_counter = int(time.time())
    stop = time.time()
    while GPIO.input(GPIO_ECHO)==1 and (int(time.time()) - timeout_counter) < 3:
        stop = time.time()

    elapsed = stop-start
    distance = elapsed * 34320
    distance = distance / 2

    return distance

bus = SMBus(1)
sensor = mlx90614.MLX90614(bus, address = 0x5A)
while True:
    range = get_range()
    if range < 30:
        print('Tolong menjauh')
        GPIO.output(GPIO_BUZZER, False)
    elif range > 50:
        print('Tolong mendekat')
        GPIO.output(GPIO_BUZZER, False)
    else:
        print('Suhu = {}'.format(round(sensor.get_object_1()+2.7,2)))
        GPIO.output (GPIO_BUZZER, True)
        #print(sensor.get_ambient())
        time.sleep(3)
