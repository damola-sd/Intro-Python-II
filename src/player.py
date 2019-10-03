# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room

class Player(Room):
    def __init__(self, name, room_name, description):
        self.name = name
        super().__init__(room_name, description)

    def __str__(self):
        return f"Player Name: {self.name}\t" + super().__str__() 

player = Player("Damola", "Foyer", "Dim light")

print(player)