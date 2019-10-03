# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room

class Player(Room):
    def __init__(self, room_name, description, name):
        self.name = name
        super().__init__(room_name, description)

    def __str__(self):
        return f"Player Name: {self.name}\t" + super().__str__() 

player = Player("Foyer", "Dim light ", "Damola")

print(player)