define narrator = Character(None, kind=nvl)
define an = DynamicCharacter('adam.name', color="#c8ffc8", kind=nvl)
define ida = DynamicCharacter('ida.name', color="#c8ffc8", kind=nvl)
define pa = Character('PA', color="#c8ffc8", kind=nvl)
define me = Character('Me', color="#c8ffc8", kind=nvl)

image display_location = DynamicDisplayable(display_location)
image display_time = DynamicDisplayable(display_time)

init python:
    
    #REMINDER: NEVER EVER PLACE STUFF THAT'S SUPPOSED TO BE SAVED IN AN INIT

    #Config setup
    menu = nvl_menu
    config.empty_window = nvl_show_core
    config.window_hide_transition = dissolve
    config.window_show_transition = dissolve
    config.nvl_paged_rollback = True
    
    #On-screen stuff
    def display_location(st, at):
        return Text(player.location, color="#ccc", size=24), .1
    def display_time(st, at):
        return Text("Day [globals.day] - [globals.time]", color="#ccc", size=24), .1

    class InventoryItem:
        def __init__(self, name):
            self.name = name
            label_name = name.lower().replace(' ', '_')
            self.examine_label = "examine_" + label_name
            self.show_label = "show_" + label_name
    
    class Inventory:
        def __init__(self, cash):
            self.cash = cash
            self.items = []
        
        def afford(self, amount):
            return self.cash >= amount
        
        def has(self, item):
            return item in self.items
        
        def add(self, item):
            self.items.append(item)
        
        def remove(self, item):
            self.items.remove(item)
        
        def examine(self, item):
            renpy.call_in_new_context(item.examine_label)

    class Char:
        def __init__(self, first_name, last_name, name, location, affection=0):
            self.first_name = first_name
            self.last_name = last_name
            self.full_name = first_name + " " + last_name
            self.name = name
            self.location = location
            self.affection = affection
            self.items_seen = []
        
        def like(self, amount):
            self.affection += amount
        
        def at(self, location):
            return location == self.location
        
        def move(self, location):
            self.location = location

    #REMINDER: NEVER EVER PLACE STUFF THAT'S SUPPOSED TO BE SAVED IN AN INIT

# The game starts here.
label start:
    window hide
    nvl show dissolve

    #Variables
    python:
        globals = {}
        globals.day = 1
        globals.time = "Evening"

        locs = {}
        locs.train_comp_6 = "Train - Compartment 6"
        locs.train_comp_7 = "Train - Compartment 7"

        stuff = {}
        stuff.home_keys = InventoryItem("Home keys")
        stuff.cellphone = InventoryItem("Cellphone")
        stuff.cd_the_wall = InventoryItem("The Wall")

        inventory = Inventory(110)
        inventory.add(stuff.home_keys)
        inventory.add(stuff.cellphone)
        inventory.add(stuff.cd_the_wall)

        chars = []
        player = Char("Kim", "Erling", "", locs.train_comp_7)
        adam = Char("Adam", "Nord", "Stranger", locs.train_comp_7)
        chars.append(adam)
        ida = Char("Ida", "Simonsson", "Stranger", locs.train_comp_6)
        chars.append(ida)

    show display_location at Position(xpos=.05, xanchor=0.0, yalign=0.9)
    show display_time at Position(xpos=.95, xanchor=1.0, yalign=0.9)
    show screen inventory_button
    show screen char_cheat_button

    jump day_1_start
