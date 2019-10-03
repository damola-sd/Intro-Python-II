from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
outside_room = room['outside']
player = Player(input("Give us your name before you embark on this journey "), outside_room)
# Write a loop that:
#

full_cardinal = {
    "n": "North",
    "e": "East",
    "s": "South",
    "w": "West",
}

def next_room(room, cardinal):
    direction = cardinal + "_to"
    # print(new_room)
    if hasattr(room, direction):
        new_room = getattr(room, direction)
        return new_room
    else:
        return False

def move_player(player, cardinal):
    current_room = next_room(player.room, cardinal)
    # print(current_room)
    if current_room:
        player.room = current_room
        print(f"You have gone {full_cardinal[cardinal]} and are now in {player.room}")
        return True
    else:
        return False

finish = False
while (finish == 0):
    print(player.room)
    move = input("Make a move in a direction ").strip().lower()
    print(player)
    if (move == "n" or move == "e" or move == "w" or move == "s"):
        next_pos = move_player(player, move)
        if next_pos:
             continue
        else: 
            print("You can't go that way")
            continue
    elif move == "quit":
        finish = True
        continue
    else: 
        print("Invalid command")
        continue

# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.