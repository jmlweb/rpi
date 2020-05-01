from gpiozero import LED, Button
from signal import pause

LED_PIN = 18
BUTTON_PIN = 24

led = LED(LED_PIN)
button = Button(BUTTON_PIN)

def toggle_led():
  if (led.is_active):
    led.off()
  else:
    led.on()

button.when_pressed = toggle_led

pause()
