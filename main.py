from ring import Colors, RingController


def main():
    ring_controller = RingController(24)
    while True:
        ring_controller.trail_wheel(Colors.GREEN, .15)


if __name__ == '__main__':
    main()
