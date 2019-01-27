import RPi.GPIO as IO

IO.setwarnings(False)
IO.setmode(IO.BCM)

leftSensor = 25
rightSensor = 24

IO.setup(leftSensor, IO.IN)
IO.setup(rightSensor, IO.IN)

def getMove():
    leftStatus = IO.input(leftSensor)
    rightStatus = IO.input(rightSensor)
    #left light right dark
    if(leftStatus==IO.LOW and rightStatus==IO.HIGH):
        return "both"
    #left dark right dark
    elif(leftStatus==IO.HIGH and rightStatus==IO.HIGH):
        return "right"
    elif(leftStatus==IO.LOW and rightStatus==IO.LOW):
        return "left"
    else:
	return "stop"
