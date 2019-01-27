
#to import libraries
import RPi.GPIO as IO
import time
import paho.mqtt.client as mqtt
import linetrack
import distancesensor
import gassensor
import motors
import camera
import threading

IO.setwarnings(False)
IO.setmode(IO.BCM)

buzzer = 6
led = 13
gasThreshold = 1
distanceThreshold = -10
isAlarm = False
isMoving = True
previousSmokeLevel = 0

IO.setup(buzzer, IO.OUT)
IO.setup(led, IO.OUT)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("alarm")
    client.subscribe("command")

def on_message(client, userdata, msg):
    print("Message Recieved")
    print(str(msg.topic),":",msg.payload)
    if str(msg.topic)=="alarm" and msg.payload == "1":
	print("Alarm Started")
        alarm(9)
    elif str(msg.topic)=="alarm" and msg.payload == "0":
        global isAlarm
        isAlarm = False
    elif str(msg.topic)=="command" and msg.payload=="stop":
	global isMoving
	print("Stop Message Recieved")
	isMoving = False

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.12.1", 1883, 60)
client.loop_start()

def main():
    global isMoving
    global distanceThreshold
    print("Device Started")
    while isMoving:
	global previousSmokeLevel
    	distance = distancesensor.readDistance()
    	if(distance<distanceThreshold):
        	motors.move('stop')
		print('stop')
        else:
        	move = linetrack.getMove()
        	print(move)
		motors.move(move)
		time.sleep(1)
        smokeLevel = gassensor.readSmokeLevel()
	if(previousSmokeLevel != smokeLevel):
		client.publish("gas", smokeLevel)
		previousSmokeLevel = smokeLevel
        if(smokeLevel>=gasThreshold):
        	alarm(smokeLevel)
        	return

def alarm(priority):
    global isAlarm
    isAlarm = True
    print("Alarm worked with priority: ",priority)
    camera.startCamera()
    t2 = threading.Thread(target=scanCamera)
    t2.start()
    while(isAlarm):
        lightBlink()
        buzzerSound()
        time.sleep(1)


def lightBlink():
    IO.output(led, IO.HIGH)
    time.sleep(1)
    IO.output(led, IO.LOW)

def buzzerSound():
    IO.output(buzzer, IO.HIGH)
    time.sleep(2)
    IO.output(buzzer, IO.LOW)
    
def scanCamera():
    global isAlarm
    while(isAlarm):
        if(camera.isPerson()):
            print("Has Person")
        else:
            print("No Person")

if __name__ == "__main__":
	t1 = threading.Thread(target=main)
	t1.start()
