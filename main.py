import ring


def main():
    while True:
        ring.trail_wheel((0, 255, 0), .15)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n\n[SIGINT] Program terminated by user.')
        ring.clear()
