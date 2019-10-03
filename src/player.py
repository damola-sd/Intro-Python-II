# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room

class Player(Room):
    def __init__(self, name, room):
        self.name = name
        self.room = room

    def __str__(self):
        return f"Player Name: {self.name}\t" + "Room Name: " + self.room.room_name + "\tDescription: " + self.room.description


room = Room("Outside", "Outside the Cave")
player = Player("Damola", room)

print(player)