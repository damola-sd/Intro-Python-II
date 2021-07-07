from room import Room
from player import Player
from item import Item
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

# Room Items
item = {
    'outside':[Item('shovel',"A need to dig away the burrow"), Item('axe','A part needs to be broken')],
    'foyer':[Item('torch',"Into the dark, yea needs the light"), Item('mask','A need to protect your nose')],
    'overlook':[Item('rope','The mountains has no stairways'), Item('hook','Hook before you leap')],
    'narrow':[Item('expander','Just a little space more for you to pass'),Item('sledge', "In case it can't be expanded it can be broken")],
    'treasure':[Item('map','Your here but to get it you need a map'), Item('shovel','Clear away the dirt')]
}

# Link rooms together
room['outside'].items = item['outside']
room['foyer'].items = item['foyer']
room['overlook'].items= item['overlook']
room['narrow'].items= item['narrow']
room['treasure'].items=item['treasure']

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# helper functions
def movePlayer(direction, current_room):
    attr = direction + "_to"

    # see if room has destination attribute
    if hasattr(current_room, attr):
        return getattr(current_room, attr)
    # else let them know they cannot go that direction
    print('You can not go that way \n')

    return current_room

# Main

# Make a new player object that is currently in the 'outside' room.

# Item list for play
items = [
    Item('knife', 'sharp blade'),
    Item('hat', 'top hat')
]

# The 'Player is Composed of a Room' <--- "HAS A" relationship
player = Player(room['outside'], items) # Composition -> "Has A" relationship

# Write a loop that:
while True:
    # * Prints the current room name
    # * Prints the current description (the textwrap module might be useful here).
    print(player.current_room)
    # * Waits for user input and decides what to do.
    command = input("Choose a direction to travel (n, s, e, w): ").strip().lower().split() # > split < split method will create a list
    # If the user enters a cardinal direction, attempt to move to the room there.
    if command[0] in ['n', 's', 'e', 'w']:
        player.current_room = movePlayer(command[0], player.current_room)
    # If the user enters "q", quit the game.
    elif command[0] == 'q':
        print('Goodbye!')
        break
    elif command[0] == 'drop':
        dropped_item = player.on_drop(command[1])
        if dropped_item is not None:
            player.current_room.on_drop(chosen_item)
    elif command[0] == 'get' or command[0] == 'take':
        chosen_item = player.current_room.on_take(command[1])
        if chosen_item is not None:
            player.on_take(chosen_item)
    # Print an error message if the movement isn't allowed.
    else:
        print("I don't recognise that command")
    

