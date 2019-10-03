from room import Room
from player import Player
from items import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance","North of you, the cave mount beckons", ),

    'foyer':    Room("Foyer", "Dim light filters in from the south. Dusty passages run north and east.",["a","a"]),

    'overlook': Room("Grand Overlook", "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.",["b"]),

    'narrow':   Room("Narrow Passage", "The narrow passage bends here from west to north. The smell of gold permeates the air."),

    'treasure': Room("Treasure Chamber", "You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.",["c"]),
}

# Declare items

items = {
    "a": Item("+1 Short Sword", "A sword with a faint blue glow"),

    "b": Item("Ring of Protection", "A ring that adds +1 to armor class and saving throws"),

    "c": Item("Cloak of Invisibility", "This cloak shimmers on one side and can't be seen from the other. Offers invisibility")
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

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

gameActive = True

name = input("What is your name Champion?:")
player = Player(name, room["outside"])

valid = ["n", "e", "s", "w" ]

while gameActive:

    print(f"\n Current Location: {player.current_room.name}")

userInput = input("Please choose the direction you'd like to explore [N] [E] [S] [W] then [Enter]: ")

if userInput in valid :
    player.move(userInput)

elif userInput == "p":
    player.addToInventory()
    print(player.inventory)

elif userInput == "q":
    gameActive = False

else: 
    print("\n Invalid Input")