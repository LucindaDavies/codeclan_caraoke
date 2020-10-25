class Room:


    def __init__(self, name, capacity):
        self.name = name
        self.guests = []
        self.songs = []
        self.capacity = capacity

    def get_name(self):
        return self.name

    def number_of_songs(self):
        return len(self.songs)

    def add_song_to_room(self, song):
        self.songs.append(song)

    def get_room_capacity(self):
        return self.capacity

    def number_of_guests(self):
        return len(self.guests)

    def how_many_songs(self):
        return len(self.songs)

    def get_capacity(self):
        return self.capacity

    def check_in_guest(self, guest):
        if len(self.guests) <= self.capacity:
                self.guests.append(guest)
        else:
            return "Sorry, no more space in this room"

    def check_out_guest(self, guest):
        self.guests.remove(guest)





