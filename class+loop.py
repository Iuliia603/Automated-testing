class Songs:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
song_lyrics = ["I ve become so numb, I can't feel you there", "Become so tired, so much more aware",
"I m becoming this, all I want to do", "Is be more like me and be less like you"]

song = Songs(song_lyrics)
song.sing_me_a_song()