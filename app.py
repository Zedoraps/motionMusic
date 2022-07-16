from datetime import datetime

from motion import Motion


def main():
    sensor = Motion()
    while True:
        print(f'{datetime.now().strftime("%H:%M:%S")}: {sensor.motion}')


if __name__ == "__main__":
    main()
