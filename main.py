from ring import Colors, RingController


def main():
    with RingController(24) as ring_controller:
        while True:
            ring_controller.trail_wheel(Colors.GREEN, .15)


if __name__ == '__main__':
    main()
