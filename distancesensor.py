import RPi.GPIO as IO
import time

IO.setwarnings(True)
IO.setmode(IO.BCM)
#analog out
echoPin = 4
triggerPin = 5

IO.setup(echoPin, IO.IN)
IO.setup(triggerPin, IO.OUT)

IO.output(triggerPin, True)
print("Distance Sensor Ready")

def readDistance():
    IO.output(triggerPin, True)
    time.sleep(0.0001)
    IO.output(triggerPin, False)
    startTime = time.time()
    stopTime = time.time()
    while(IO.input(echoPin)==0):
        startTime = time.time()

    while(IO.input(echoPin)==1):
        stopTime = time.time()
    #time difference between start and arrival
    timeElapsed = stopTime - startTime
    #sonic speed 34300
    distance = (timeElapsed*17150)
    print("Distance: ",round(distance, 2))
    return distance
    
