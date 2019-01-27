import RPi.GPIO as IO
import time

IO.setwarnings(False)
IO.setmode(IO.BCM)

left_b = 7
left_a = 8
left_en = 11
right_a = 16 
right_b = 20
right_en = 21

IO.setup(left_a, IO.OUT)
IO.setup(left_b, IO.OUT)
IO.setup(left_en, IO.OUT)
IO.setup(right_a, IO.OUT)
IO.setup(right_b, IO.OUT)
IO.setup(right_en, IO.OUT)
p_right_en = IO.PWM(right_en, 100)
p_right_a = IO.PWM(right_a, 100)
p_right_b = IO.PWM(right_b, 100)
p_left_en = IO.PWM(left_en, 100)
p_left_a = IO.PWM(left_a, 100)
p_left_b = IO.PWM(left_b, 100)

def move(movement):
    if movement=='both':
	p_right_en.start(60)
	p_left_en.start(60)
	p_right_a.start(100)
	p_left_a.start(100)
	p_left_b.start(0)
	p_right_b.start(0)
	time.sleep(0.8)
	move('stop')
    elif movement=='right':
	p_right_en.start(60)
        p_right_a.start(100)
        p_right_b.start(0)
	p_left_en.start(0)
	p_left_a.start(0)
	p_left_b.start(0)
	time.sleep(0.8)
	move('stop')
    elif movement=='left':
        p_left_en.start(60)
	p_left_a.start(100)
	p_left_b.start(0)
	p_right_en.start(0)
	p_right_a.start(0)
	p_right_b.start(0)
	time.sleep(0.8)
	move('stop')
    elif movement=='stop':
        p_left_en.start(0)
	p_left_a.start(0)
	p_left_b.start(0)
	p_right_en.start(0)
	p_right_a.start(0)
	p_right_b.start(0)
	time.sleep(2)
