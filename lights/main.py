from gpiozero import LED, Button
from signal import pause

LED_PIN = 18
BUTTON_PIN = 24
MODES = ['fixed', 'blink']

led = LED(LED_PIN)
button = Button(BUTTON_PIN)
next_mode = MODES[0]

def toggle_led():
  if (led.is_active):
    led.off()
  elif (next_mode == MODES[0]):
    next_mode = MODES[1]
    led.on()
  else:
    next_mode = MODES[0]
    led.blink(0.5, 0.5)

button.when_pressed = toggle_led

pause()
