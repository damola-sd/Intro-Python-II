# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
  def __init__ (self, room, inventory=[]):
    self.current_room = room
    self.inventory = inventory

  def on_take(self, item):
    self.inventory.append(item)
    print("This player has picked up " + item.name)

  def on_drop(self, item_name):
    wanted_items = []
    chosen_item = None
    for item in self.inventory:
      if item.name == item_name:
        chosen_item = item
      else:
        wanted_items.append(item)
    self.inventory = wanted_items

    if chosen_item is None:
      print("This player doesn't have that " + item_name)
    else:
      print("This player has dropped the ", chosen_item.name)
      return chosen_item