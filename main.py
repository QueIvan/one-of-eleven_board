from ring import RingController


def main():
    ring_controller = RingController(24)
    while True:
        ring_controller.trail_wheel((255, 0, 0), .15)


if __name__ == '__main__':
    main()
