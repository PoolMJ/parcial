import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt 
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)

def lectura(ms):
    client.publish("nelsonbenjamin05@gmail.com/ts1",ms)
            
def conexion(client,userdata,flags,rc):
    print("Conectado")

def recepcion(client,userdata,msg):
    msgr=str(msg.payload.decode("utf-8"))
    if msgr == 'on':
        GPIO.output(7, True)
    if msgr == 'off':
        GPIO.output(7, False)
    
client=mqtt.Client() 
client.on_connect=conexion
client.on_message=recepcion
client.username_pw_set("nelsonbenjamin05@gmail.com","123456789") 
client.connect("maqiatto.com", 1883)
client.subscribe("nelsonbenjamin05@gmail.com/ts", 0)
         
def main():
    rc=0
    while rc==0:
        lectura(1)
        time.sleep(1)
        rc=client.loop()