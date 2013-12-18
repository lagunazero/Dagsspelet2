#Always use call for this, with the character we're showing an item to passed along.
label menu_show_items(char):
    nvl clear
    python:
        
        choices = [("None", "")]
        #Add all inventory items as tuples of displayable and result
        for item in inventory.items:
            choices.append((item.name, item))

    #Uses nvl_menu here instead of renpy.display_menu because the other one uses adv style menu
    $ item = nvl_menu(choices)
    #Loop around here until the user presses None.
    #TODO: Should probably enable escaping here from some items too.
    while item != "":
        $ result = item.show_label + "_" + char.first_name.lower()
        if item in char.items_seen:
            $ result = result + "_again"
        else:
            $ char.items_seen.append(item)
        nvl clear
        #Use call so we'll continue looping.
        call expression result
        $ item = nvl_menu(choices)
    jump menu_show_items_end

label menu_show_items_end:
    nvl clear
    return

#-----------------------------------EXAMINE-----------------------------------

#------------------------------------HOME KEYS
label examine_home_keys:
    "examine keys"
    return

#------------------------------------CELLPHONE
label examine_cellphone:
    "cellphone"
    return

#------------------------------------THE WALL
label examine_the_wall:
    "the wall"
    return

#------------------------------------BRAVE NEW WORLD
label examine_brave_new_world:
    "bnw"
    return


#------------------------------------SHOW-------------------------------------

#------------------------------------HOME KEYS
label show_home_keys_adam:
    "show keys to adam"
    return

label show_home_keys_adam_again:
    "show keys to adam again"
    return

label show_home_keys_ida:
    "show keys to ida"
    return

label show_home_keys_ida_again:
    "show keys to ida"
    return

#------------------------------------CELLPHONE
label show_cellphone_adam:
    "show cell to adam"
    return

label show_cellphone_adam_again:
    "show cell to adam"
    return

label show_cellphone_ida:
    "show cell to ida"
    return

label show_cellphone_ida_again:
    "show cell to ida"
    return

#------------------------------------THE WALL
label show_the_wall_adam:
    "show wall to adam"
    return

label show_the_wall_adam_again:
    "show wall to adam"
    return

label show_the_wall_ida:
    "show wall to ida"
    return

label show_the_wall_ida_again:
    "show wall to ida"
    return

#------------------------------------BRAVE NEW WORLD
label show_brave_new_world_adam:
    $ adam.like(2)
    "show bnw to adam first"
    return

label show_brave_new_world_adam_again:
    "show bnw to adam again"
    return

label show_brave_new_world_ida:
    "show bnw to ida"
    return

label show_brave_new_world_ida_again:
    "show bnw to ida"
    return
