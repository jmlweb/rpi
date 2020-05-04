from gpiozero import LightSensor
from time import sleep

sensor = LightSensor(18, 5, 0.66)

while True:
    print(sensor.value())
    sleep(0.5)
