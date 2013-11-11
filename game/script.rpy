# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
#TODO Character names + colors
define narrator = Character(None, kind=nvl)
define an = DynamicCharacter('an_name', color="#c8ffc8", kind=nvl)
define pa = Character('PA', color="#c8ffc8", kind=nvl)
define me = Character('Me', color="#c8ffc8", kind=nvl)

init python:

    menu = nvl_menu
    config.empty_window = nvl_show_core
    config.window_hide_transition = dissolve
    config.window_show_transition = dissolve
    config.nvl_paged_rollback = True

# The game starts here.
label start:
    window hide
    nvl show dissolve

    $ player_name = ""
    $ an_name = "Stranger"
    $ an_like = 0
    $ an_location = "train_compartment"

    jump day_1_start
