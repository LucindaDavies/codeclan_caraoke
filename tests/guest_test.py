import unittest

from classes.guest import Guest
from classes.song import Song

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.song1 = Song("Help", "The Beatles")
        self.song2 = Song("Saturday Night", "Sam Cooke")

        self._songs = [self.song1, self.song2]

        self.guest = Guest("Hannah")

    def test_guest_has_name(self):
        self.assertEqual("Hannah", self.guest.get_name())

    