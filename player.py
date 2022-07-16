import os


class Player:

    def __init__(self, path):
        self.path = path
        songs = []
        for file in os.listdir(path):
            if file.endswith('.mp3'):
                songs.append(file)
        print(f"found the following songs {len(songs)}: {', '.join(songs)} ")

    def play_if_not_already_playing(self):

        pass
