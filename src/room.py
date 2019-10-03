# Implement a class to hold room information. This should have name and
# description attributes.
class Room():
    def __init__(self, name, description):
        self.room_name = name
        self.description = description

    
    def __str__(self):
        return "Room: " + self.room_name + "\t Description: " + self.description
    
