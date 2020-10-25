import unittest

from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.song1 = Song("Help", "The Beatles")
        self.song2 = Song("Saturday Night", "Sam Cooke")
       

        self.songs = [self.song1, self.song2]

        self.guest1 = Guest("Hannah")
        self.guest2 = Guest("Louise")
        self.guest3 = Guest("Harry")

        self.guests = [self.guest1, self.guest2, self.guest3]

        self.room = Room("Motown", 3)


    def test_room_has_name(self):
        self.assertEqual("Motown", self.room.get_name())

    def test_can_add_song(self):
        song = self.song2
        self.room.add_song_to_room(song)
        self.assertEqual(1, self.room.number_of_songs())


    def test_can_check_in_guest(self):
        self.room.check_in_guest(self.guest1)
        self.assertEqual(1, self.room.number_of_guests())

    def test_room_has_capacity(self):
        self.assertEqual(3, self.room.get_capacity())
    
    def test_can_check_guest_out(self):
        self.room.check_in_guest(self.guest3)
        self.room.check_out_guest(self.guest3)
        self.assertEqual(0, self.room.number_of_guests())

    




