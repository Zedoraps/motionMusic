import time
from datetime import datetime

from motion import Motion


def on_motion():
    print("Would start playing now!")


def main():
    sensor = Motion(on_motion)
    while True:
        time.sleep(1)
        print(f'{datetime.now().strftime("%H:%M:%S")}: {sensor.motion}')


if __name__ == "__main__":
    main()
