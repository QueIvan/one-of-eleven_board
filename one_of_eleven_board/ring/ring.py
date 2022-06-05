from dataclasses import dataclass
import time
import math
import board
import neopixel
import numpy as np


class Colors:
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    CYAN = (0, 255, 255)
    MAGENTA = (255, 0, 255)
    WHITE = (255, 255, 255)
    OFF = (0, 0, 0)


@dataclass
class RingController:
    __number_of_leds: int
    __brightness: float = .05
    __start_led_index = 0

    def __post_init__(self):
        self.__leds = neopixel.NeoPixel(board.D18, self.__number_of_leds, brightness=float(self.__brightness),
                                        auto_write=False, pixel_order=neopixel.GRB)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.clear()

    def set_pixel(self, led_id: int, color: tuple) -> None:
        self.__leds[led_id] = color if led_id != 6 else (color[1], color[0], color[2])
        self.__leds.show()

    def step_fade_out(self, starting_color: tuple, step_down_percentage: float, current_step_count: int) -> tuple:
        starting_color = np.array(starting_color)
        target_color = np.array(Colors.OFF)
        vector = target_color - starting_color
        result = starting_color + vector * step_down_percentage * current_step_count\
            if min(starting_color + vector * step_down_percentage * current_step_count) >= 0 else Colors.OFF
        return tuple(np.array(np.rint(result), dtype=int))

    def create_trail(self, color: tuple, trail_length: int, step_down_percentage: float, led_ids: tuple) -> None:
        if len(led_ids) > 0:
            for led in led_ids:
                step_count = led_ids.index(led) if min(led_ids) < self.__number_of_leds - (trail_length + 1) \
                    else led_ids.index(led) + (trail_length + 1) - len(led_ids)
                self.set_pixel(led, self.step_fade_out(color, step_down_percentage, step_count))
            self.__leds.show()

    def pixel_fill(self, color: tuple) -> None:
        self.__leds.fill(color if type(color) is tuple else (color, color, color))
        self.__leds[6] = (color[1], color[0], color[2]) if type(color) is tuple else (color, color, color)
        self.__leds.show()

    def set_brightness(self, brightness: float) -> None:
        self.__leds.brightness = brightness
        self.__leds.show()
        time.sleep(.05)

    def flash_brightness(self, target_value: float, color: tuple = None) -> None:
        if color is not None:
            self.pixel_fill(color)
        [self.set_brightness(round(i / 100, 2)) for i in range(int(self.__brightness * 100), int(target_value * 100), 5)]
        [self.set_brightness(round(i / 100, 2)) for i in
         range(int(target_value * 100), int(self.__brightness * 100), -5)]
        self.set_brightness(self.__brightness)

    def trail_wheel(self, color: tuple, step_down_percentage: float, more_than_one_loop: bool = True) -> None:
        trail_length = math.ceil(max(color) / (max(color) * step_down_percentage))
        for trail_start_id in range(self.__start_led_index, self.__number_of_leds + trail_length):
            trail_led_ids = self.get_index_seq(trail_start_id, trail_length, more_than_one_loop)
            self.create_trail(color, trail_length, step_down_percentage, trail_led_ids)
            time.sleep(.05)

    def get_index_seq(self, trail_start_id: int, trail_length: int, more_than_one_loop: bool) -> tuple:
        led_ids = ()
        for i in range(trail_length + 1):
            if 0 <= trail_start_id - i < self.__number_of_leds:
                led_ids += (trail_start_id - i,)
            elif trail_start_id - i >= self.__number_of_leds and more_than_one_loop:
                self.__start_led_index = trail_length
                led_ids += (trail_start_id - i - self.__number_of_leds,)
        return led_ids

    def clear(self) -> None:
        self.__leds.fill(Colors.OFF)
        self.__leds.show()
