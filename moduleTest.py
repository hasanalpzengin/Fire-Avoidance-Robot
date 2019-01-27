from hcsr04sensor import sensor

trig_pin = 5
echo_pin = 4

value = sensor.Measurement(trig_pin, echo_pin)
raw_measurement = value.raw_distance()

metric_distance = value.distance_metric(raw_measurement)
print("The Distance = {} centimeters".format(metric_distance))
