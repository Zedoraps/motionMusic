import time
from datetime import datetime, timedelta
from threading import Thread

from motion import Motion
from player import Player


class Manager:
    sensor_thread = None

    def __init__(self):
        self.stop_time = datetime.now()
        self.player = Player("/home/croc/Desktop/croc/songs")
        self.sensor = Motion(self.on_motion)

    def start_player(self):
        if self.sensor_thread is not None:
            return "Already running"
        else:
            self.sensor.start()
            print("starting new thread for the sensing")
            sensor_thread = Thread(target=self.sens())
            sensor_thread.start()
            return 'Started'

    def on_motion(self):
        self.player.play_or_continue_playing()
        self.stop_time = datetime.now() + timedelta(seconds=10)

    def sens(self):
        while True:
            time.sleep(1)
            print(
                f'{datetime.now().strftime("%H:%M:%S")}: {self.player.info()} end at: {self.stop_time.strftime("%H:%M:%S")}')
            if self.stop_time < datetime.now():
                print("End time reached")
                self.player.stop()

    def stop(self):
        self.player.stop()
