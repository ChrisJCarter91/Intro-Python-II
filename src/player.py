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
                f"NEAR BY ITEMS: {self.current_room.item}")
        else:
            print(f"\nThere is a wall there, choose another direction\n")

    def addToInventory(self):
        removedItem = self.current_room.item.pop()
        addedItem = self.inventory.append(removedItem)
        return addedItem