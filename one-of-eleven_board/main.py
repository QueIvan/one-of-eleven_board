from ring import Colors, RingController


def main():
    with RingController(24, .05) as ring_controller:
        ring_controller.trail_wheel(Colors.RED, .15, False)
        ring_controller.flash_brightness(.55, Colors.RED)
        ring_controller.clear()


if __name__ == '__main__':
    main()
