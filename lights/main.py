from gpiozero import LED
from time import sleep

LED_PIN = 18

led = LED(LED_PIN)

def turn_on():
  led.on()

def turn_off():
  led.off()

while True:
  turn_on()
  sleep(1)
  turn_off()
  sleep(1)
