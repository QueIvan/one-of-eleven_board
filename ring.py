import time
import math
import board
import neopixel
import numpy as np

num_pixels = 24
pixels = neopixel.NeoPixel(board.D18, num_pixels, brightness=0.05, auto_write=False, pixel_order=neopixel.GRB)
start_id = 0
number = 0


# ********************
#
#  Ready functions
#
# ********************

def set_pixel(index, color):
    pixels[index] = color if index != 6 else (color[1], color[0], color[2])
    pixels.show()


def step_fade_out(color, percent, step):
    color = np.array(color)
    target = np.array([0, 0, 0])
    vector = target - color
    result = color + vector * percent * step if min(color + vector * percent * step) >= 0 else (0, 0, 0)
    return tuple(np.array(np.rint(result), dtype=int))


def create_trail(color, multiplier, ids):
    if len(ids) > 0:
        for j in ids:
            step_count = ids.index(j) if min(ids) < num_pixels - (number + 1) else ids.index(j) + (number + 1) - len(
                ids)
            set_pixel(j, step_fade_out(color, multiplier, step_count))
        pixels.show()


def pixel_fill(color):
    pixels.fill(color if type(color) is tuple else (color, color, color))
    pixels[6] = (color[1], color[0], color[2]) if type(color) is tuple else (color, color, color)
    pixels.show()


def set_brightness(brightness):
    pixels.brightness = brightness / 100
    pixels.show()
    time.sleep(.05)


def flash_brightness(high_value):
    store_brightness = pixels.brightness * 100
    set_brightness(high_value)
    for i in range(0, high_value, 5):
        set_brightness((high_value - i))
    set_brightness(store_brightness)


def trail_wheel(color, multiplier):
    global number
    number = math.ceil(max(color) / (max(color) * multiplier))
    for i in range(start_id, num_pixels + number):
        ids = get_index_seq(i)
        create_trail(color, multiplier, ids)
        time.sleep(.05)


def get_index_seq(index):
    global start_id
    indexes = ()
    for i in range(number + 1):
        if 0 <= index - i < num_pixels:
            indexes += (index - i,)
        elif index - i >= num_pixels:
            start_id = number
            indexes += (index - i - num_pixels,)
    return indexes


def clear():
    pixels.fill((0, 0, 0))
    pixels.show()


# ********************
#
#  Dev Work
#
# ********************

def test():
    pixel_fill((0, 0, 0))
