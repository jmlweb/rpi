from time import time, sleep
from signal import pause
from random import randint
from gpiozero import LED, RGBLED, Button

from game_typings import Options
from game_buttons import GameButtons
from game_indicators import GameIndicators
from game_result import GameResult
from game import Game

DELAY_MIN = 0
DELAY_MAX = 7

PIN_LED_A = 18
PIN_LED_B = 19
PIN_BUTTON_A = 17
PIN_BUTTON_B = 16

PIN_RGBLED = [22, 23, 24]

TIME_LIMIT = 1.5


class Main:
    def __init__(self, options: Options, result_led: RGBLED):
        self.starting_time = 0
        self.options = options
        self.game_indicators = GameIndicators(options)
        self.game_result = GameResult(result_led)
        self.game = Game(options, self.on_new_question, self.on_ok, self.on_ko)
        self.game_buttons = GameButtons(options, self.game.process_answer)
        self.new_turn()

    def new_turn(self):
        self.game_indicators.reset()
        sleep(1)
        self.game_result.reset()
        new_timeout = randint(DELAY_MIN, DELAY_MAX)
        sleep(new_timeout)
        self.game.choose_question()

    def on_new_question(self):
        self.game_indicators.select(self.game.current_question)
        self.starting_time = time()

    def on_ok(self):
        self.game_indicators.reset()
        total_time = time() - self.starting_time
        is_success = total_time < TIME_LIMIT
        fn = self.game_result.success if (
            is_success
        ) else self.game_result.warn
        fn()
        self.new_turn()

    def on_ko(self):
        self.game_result.error()
        self.new_turn()


def run():
    options = {
        "a": {
            "indicator": LED(PIN_LED_A),
            "button": Button(PIN_BUTTON_A)
        },
        "b": {
            "indicator": LED(PIN_LED_B),
            "button": Button(PIN_BUTTON_B)
        }
    }
    main = Main(options, RGBLED(*PIN_RGBLED))
    pause()


if __name__ == "__main__":
    run()
