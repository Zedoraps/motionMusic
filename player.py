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
            index = random.randint(0, len(self.songs) - 1)
            self.player = vlc.MediaPlayer(f"{self.path}/{self.songs[index]}")
            self.player.play()
        else:
            print("No songs to play!")
