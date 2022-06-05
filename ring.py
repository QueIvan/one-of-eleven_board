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


class RingController:

    def __init__(self, num_pixels):
        self.__num_pixels = num_pixels
        self.__pixels = neopixel.NeoPixel(board.D18, num_pixels, brightness=0.05, auto_write=False,
                                          pixel_order=neopixel.GRB)
        self.__start_id = 0
        self.__number = 0

    def __del__(self):
        self.__pixels.fill(Colors.OFF)
        self.__pixels.show()

    # ********************
    #
    #  Ready functions
    #
    # ********************

    def set_pixel(self, index, color):
        self.__pixels[index] = color if index != 6 else (color[1], color[0], color[2])
        self.__pixels.show()

    @staticmethod
    def step_fade_out(color, percent, step):
        color = np.array(color)
        target = np.array(Colors.OFF)
        vector = target - color
        result = color + vector * percent * step if min(color + vector * percent * step) >= 0 else Colors.OFF
        return tuple(np.array(np.rint(result), dtype=int))

    def create_trail(self, color, multiplier, ids):
        if len(ids) > 0:
            for j in ids:
                step_count = ids.index(j) if min(ids) < self.__num_pixels - (self.__number + 1) else ids.index(j) + (
                        self.__number + 1) - len(
                    ids)
                self.set_pixel(j, self.step_fade_out(color, multiplier, step_count))
            self.__pixels.show()

    def pixel_fill(self, color):
        self.__pixels.fill(color if type(color) is tuple else (color, color, color))
        self.__pixels[6] = (color[1], color[0], color[2]) if type(color) is tuple else (color, color, color)
        self.__pixels.show()

    def set_brightness(self, brightness):
        self.__pixels.brightness = brightness / 100
        self.__pixels.show()
        time.sleep(.05)

    def flash_brightness(self, high_value):
        store_brightness = self.__pixels.brightness * 100
        self.set_brightness(high_value)
        for i in range(0, high_value, 5):
            self.set_brightness((high_value - i))
        self.set_brightness(store_brightness)

    def trail_wheel(self, color, multiplier):
        self.__number = math.ceil(max(color) / (max(color) * multiplier))
        for i in range(self.__start_id, self.__num_pixels + self.__number):
            ids = self.get_index_seq(i)
            self.create_trail(color, multiplier, ids)
            time.sleep(.05)

    def get_index_seq(self, index):
        indexes = ()
        for i in range(self.__number + 1):
            if 0 <= index - i < self.__num_pixels:
                indexes += (index - i,)
            elif index - i >= self.__num_pixels:
                self.__start_id = self.__number
                indexes += (index - i - self.__num_pixels,)
        return indexes

    def clear(self):
        self.__pixels.fill(Colors.OFF)
        self.__pixels.show()
