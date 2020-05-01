from gpiozero import LED, Button
from signal import pause

class Mode:
  def __init__(self, name, operation, next = None):
    self.name = name
    self.operation = operation
    self.next = next

class Modes:
  def __init__(self, led):
    blink_mode = Mode("blink", lambda led: led.blink(0.2, 0.2))
    enable_mode = Mode("enable", lambda led: led.on(), blink_mode)
    disable_mode = Mode("disable", lambda led: led.off(), enable_mode)
    blink_mode.next = disable_mode
    self.current = disable_mode
    self.led = led

  def toggle(self):
    self.current = self.current.next
    self.current.operation(self.led)

LED_PIN = 18
BUTTON_PIN = 24

led = LED(LED_PIN)
button = Button(BUTTON_PIN)

modes = Modes(led)

button.when_pressed = modes.toggle

pause()
