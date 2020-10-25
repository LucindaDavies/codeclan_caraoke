import unittest
from classes.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Help", "The Beatles")

    def test_song_has_title(self):
        self.assertEqual("Help", self.song.get_title())

    def test_song_has_artist(self):
        self.assertEqual("The Beatles", self.song.get_artist())