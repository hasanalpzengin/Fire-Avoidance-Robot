import RPi.GPIO as IO

IO.setwarnings(False)
IO.setmode(IO.BCM)
#digital out
digitalPin = 3
IO.setup(digitalPin, IO.IN, pull_up_down=IO.PUD_DOWN)
smokeLevel = 0

def set_smoke_level(pin):
	global smokeLevel
	smokeLevel = 1

IO.add_event_detect(digitalPin, IO.RISING)
IO.add_event_callback(digitalPin, set_smoke_level)

def readSmokeLevel():
    global smokeLevel
    print("Smoke Level: ",smokeLevel)
    return smokeLevel
