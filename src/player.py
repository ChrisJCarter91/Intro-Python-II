# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room, inventory =[]):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def __str__(self):
        return f"PLAYER: {self.name}\nLOCATION: {self.current_room}"

    def move(self,direction):
        if getattr(self.current_room, f"{direction}_to") is not None:
            self.current_room = getattr(self.current_room, f"{direction}_to")
            print(f"\nLOCATION: {self.current_room.name}\n"
                f"DESCRIPTION: {self.current_room.description}\n"
                f"NEARBY ITEMS: {self.current_room.item}")
        else:
            print(f"\nThere is a wall there, choose another direction\n")

    def looting(self, loot):
        loot = loot.split(" ")
        if loot[0] == "take":
            if loot[1] in self.current_room.item:
                self.current_room.item.remove(loot[1])
                self.inventory.append(loot[1])
                return print (f"You have looted {loot[1]}")
            else:
                print("Unable to Loot")
        elif loot[0] == "drop":
            if loot[1] not in self.current_room.item:
                self.inventory.remove(loot[1])
                self.current_room.item.append(loot[1])
                return print(f"You have dropped {loot[1]}")
            else: 
                print("You Don't Have That Item To Drop")