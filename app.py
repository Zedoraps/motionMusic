import time
from datetime import datetime, timedelta

from motion import Motion
from player import Player

stop_time = datetime.now()


def main():
    player = Player("/home/croc/Desktop/croc/songs")

    def on_motion():
        player.play_or_continue_playing()
        global stop_time
        stop_time = datetime.now() + timedelta(seconds=10)

    sensor = Motion(on_motion)
    while True:
        time.sleep(1)
        print(f'{datetime.now().strftime("%H:%M:%S")}: {player.info()} end at: {stop_time.strftime("%H:%M:%S")}')
        if stop_time < datetime.now():
            print("End time reached")
            player.stop()


if __name__ == "__main__":
    main()
