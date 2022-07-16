import os
import random

import vlc


class Player:

    def __init__(self, path):
        self.path = path
        self.songs = []
        self.player = None
        for file in os.listdir(path):
            if file.endswith('.mp3'):
                self.songs.append(file)
        print(f"found the following songs {len(self.songs)}: {', '.join(self.songs)} ")

    def play_or_continue_playing(self):
        if len(self.songs) > 0:
            if self.player and self.player.is_playing():
                print("already playing")
            else:
                index = random.randint(0, len(self.songs) - 1)
                print(f"start playing: {self.path}/{self.songs[index]}")
                self.player = vlc.MediaPlayer(f"file://{self.path}/{self.songs[index]}")
                self.player.play()
        else:
            print("No songs to play!")

    def stop(self):
        if self.player and self.player.is_playing():
            print("stopped playing")
            self.player.stop()

    def info(self):
        if self.player:
            return f"{self.player.get_time() / 1000} / {self.player.get_length() / 1000}"
        else:
            return "No player present"
