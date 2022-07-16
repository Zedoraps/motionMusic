import time
from datetime import datetime

from motion import Motion
from player import Player


def main():
    player = Player("/home/croc/Desktop/croc/songs")

    def on_motion():
        player.play_if_not_already_playing()

    sensor = Motion(on_motion)
    while True:
        time.sleep(1)
        print(f'{datetime.now().strftime("%H:%M:%S")}: {sensor.motion}')


if __name__ == "__main__":
    main()
