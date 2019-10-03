# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
  def __init__ (self, name, description, items=None):
    self.name = name
    self.description = description
    self.items = None

    if items == None:
      self.items = []

  def on_take(self, item_name):
    unwanted_items = []
    chosen_item = None
    for item in self.items:
      if item.name == item_name: # Item doesn't get added to unwanted_items
        chosen_item = item
      else: # Item get's added to unwanted_items
        unwanted_items.append(item)
    self.items = unwanted_items

    if chosen_item is None:
      print("This room doesn't have a " + item_name)
    else:
      return chosen_item

  def on_drop(self, item):
    self.items.append(item)
      

  def __str__ (self):
    item_string = ""

    for item in self.items:
      item_string += f'{item.name} '
    return f'\n{self.name} - {self.description}\n This room has these items: {item_string}\n'