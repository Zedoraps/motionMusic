import os
import random
import time

import vlc


class Player:

    def __init__(self, path):
        self.path = path
        self.songs = []
        self.player = None
        self.counter = 30
        for file in os.listdir(path):
            if file.endswith('.mp3'):
                self.songs.append(file)
        print(f"found the following songs {len(self.songs)}: {', '.join(self.songs)} ")

    def play_or_continue_playing(self):
        if len(self.songs) > 0:
            if self.player and self.player.is_playing():
                if self.counter > 10:
                    print("Reset Time to 30 Seconds")
                    self.counter = 30
                else:
                    print("adding 20 seconds to the current player")
                    self.counter += 20
            else:
                index = random.randint(0, len(self.songs) - 1)
                self.player = vlc.MediaPlayer(f"{self.path}/{self.songs[index]}")
                self.player.play()
                while self.counter > 0:
                    self.counter -= 1
                    time.sleep(1)

                self.player.stop()
        else:
            print("No songs to play!")
