label adam_pa_delay_ask_hurry:
    nvl clear
    me "You're in a hurry?"
    an "Hah! That's supposed to be a joke?"
    me "Didn't plan it that way. Probably would have phrased it differently in that case."
    menu:
        "Make a pun":
            $ an_like -= 1
            me "Maybe: Yes, it IS quite late. It's dusk already!"
            "The man goes silent and motionless."
        "Don't":
            ""
    nvl clear
    an "Yes, I'm in a hurry. Otherwise I wouldn't be taking the train."
    an "Why, aren't you?"
    menu:
        "\"Not particularly\"":
            me "Not particularly."
        "\"I'll need to reach Ashton eventually, but to be honest I'm not looking forward to it\"":
            me "I'll need to reach Ashton eventually, but to be honest I'm not looking forward to it."
    an "Hrmm. Well I'm not entitled to be as carefree as you."
    an "And on that topic... Go ask a conductor what's holding us, would you?"
    menu:
        "\"Well, alright then\"":
            $ d1_adam_ask_conductor = "agreed"
            $ an_like += 2
            nvl clear
            me "Well, alright then."
            "The man blinks, then straightens up and picks his book up."
            "After a stern nod at me he resumes reading again."
            jump menu_train_compartment
        "\"Why don't you do it yourself?\"":
            nvl clear
            me "Why don't you do it yourself?"
            an "Hrmm."
            an "Because unlike some people, I have luggage with me."
            "He gestures at a suitcase lying on the luggage rack, then at the book in his hand."
            an "And I can't very well leave it alone."
            me "Right... So me being here wouldn't solve that?"
            an ".........."
            nvl clear
            an "Are you going to check with the conductor or not?"
            menu:
                "\"I suppose I could\"":
                    $ d1_adam_ask_conductor = "agreed"
                    $ an_like += 1
                    nvl clear
                    me "I suppose I could."
                    "The man blinks, then straightens up and picks his book up."
                    "After a stern nod at me he resumes reading again."
                    jump menu_train_compartment
                "\"Nope\"":
                    $ d1_adam_ask_conductor = "refused"
                    $ an_like -= 2
                    $ an_location = "train_dining_car"
                    nvl clear
                    me "Nope."
                    "The man's fists tightens and I can see a vein being added to his forehead."
                    an "Fine. Fine!"
                    "He struggles violently with getting his suitcase off the luggage rack for about a minute before it finally plumps down onto his back. Responding with only a groan, he then proceeds to stuff the book into a pocket on the side of the suitcase and clampers out of the compartment."
                    nvl clear
                    "He rams the sliding door shut behind him and I can hear his steps thunder away."
                    "The silence that follows is almost deafening."
                    jump menu_train_compartment

#TODO content
label adam_pa_delay_chill:
    nvl clear
    me "Chill, man."


label bother_adam_talking:
    nvl clear
    an "What is it you want?"
    menu:
        "\"Umm... I was bored, I guess?\"":
            jump adam_talk_bored
        "\"What're you reading?\"":
            jump adam_talk_reading
        "\"Just talk for a bit. We're stuck here together, after all.\"":
            jump adam_talk_chitchat
        "\"Seen this book?\" Hold out Brave New World" if d1_dining_car_book_taken:
            jump adam_talk_bnw

label adam_talk_bored:
    nvl clear
    $ an_like -= 1
    an "I don't see how that's any of my concern."
    "He sighs hyperbolically, to overstate his lack of interest."
    menu:
        "\"I suppose so. You've got a book to read, at least.\"":
            jump adam_talk_reading
        "\"It's quite pretty out the window, though.\"" if d1_compartment_window_seen:
            jump adam_talk_window
        "\"It is your concern because it means I'm forced to bother you like this.\"":
            jump adam_talk_bored_2

label adam_talk_bored_2:
    $ an_like -= 1
    nvl clear
    an "I don't see how anything forces you to do such a thing. Now could you please leave me be?"
    "He opens the book back up. His finger must have been acting a bookmark the whole time."
    menu:
        "\"Yeah, you go back to reading your book. See if I care!\"":
            jump adam_talk_bored_3
        "\"Look, I think we got off on the wrong foot here. Since we're sharing the compartment, let's at least introduce ourselves.\"":
            jump adam_talk_introduce

label adam_talk_bored_3:
    $ an_like -= 2
    nvl clear
    an "Yes! Yes! I think I just will do just that, thank you very much for your insightful suggestion!"
    "He slams the book in between us and puts his legs up on the seat, like a shield. His fingers clamp hard on each side of the book."
    "In the silence that follows I can hear what I can only assume to be his teeth gnashing."
    nvl clear
    "A few minutes pass in increasingly uncomfortable silence."
    "I notice that he hasn't turned a single page since he brought the book back up."
    menu:
        "\"Alright, listen. I'm sorry. I didn't mean to brush you off like that.\"":
            $ an_like += 1
            jump adam_talk_introduce
        "\"Hey man, don't be like that. Can we start this over?\"":
            jump adam_talk_introduce
        "\"You're not really reading, are you?\"":
            jump adam_talk_bored_4

label adam_talk_bored_4:
    $ an_like -= 1
    nvl clear
    an "............"
    "He puts the book back down and just stare at me."
    "Eventually he takes off his glasses and hold them so hard I begin to fear they'll crack."
    "Though, on second thought, he looks weak enough that that might not be an issue."
    nvl clear
    an "What I have done to deserve a fate like this?"
    "I don't think the question was aimed at me, so I keep my silence."
    "After a moment of eye-rolling, he again aims his stare straight at me and takes on a serious frown."
    an "Aren't there any other places you can be? This is a large train, you know."
    menu:
        "\"Nope, the other rooms are locked.\"" if d1_neighbour_compartment_seen_lock:
            an "Figures you'd already snooped around."
        "\"The dining car is a deserted dump. So no, not really.\"" if d1_dining_car_seen:
            an "Sounds like that'd be good fit, in my opinion..."
        "\"I don't know, but this is my seat so we might as well get along.\"" if d1_dining_car_seen == False and d1_neighbour_compartment_seen_lock == False:
            an "And this how you get along with people?"
    an "Fiiiiine. I'll give you one more, wholly undeserved, chance."
    jump adam_talk_introduce

label adam_talk_window:
    $ an_like -= 1
    nvl clear
    an "Yes, very."
    "I could be wrong, but he does not appear entirely sincere as he does not for even a moment glance out the window."
    menu:
        "\"Notice how the sunset makes the forest silhoutte stand out?\"":
            jump adam_talk_window_2
        "\"Alright, sorry. I can see this isn't your topic of choice. We can talk about something else instead.\"":
            jump adam_talk_chitchat

#TODO content
label adam_talk_window_2:
    $ an_like -= 1
    nvl clear
    
label adam_talk_chitchat:
    $ an_like -= 1
    nvl clear
    an "I fail to see the merit of idle chitchat. If you have something to discuss with me, just bring it up instead of wasting my time."
    menu:
        "\"Well, what about that book of yours?\"" if d1_adam_discussed_book == False:
            jump adam_talk_reading
        "\"Maybe we can talk about this?\" Hold out Brave New World" if d1_dining_car_book_taken and d1_adam_shown_bnw == False:
            jump adam_talk_bnw
        "\"We could start by just introducing ourselves? A fairly orthodox start, right?\"" if d1_adam_introduced == False:
            jump adam_talk_introduce
    
label adam_talk_introduce:
    $ d1_adam_introduced = True
    nvl clear
    "He raps his fingers a couple times across the cover of the book."
    an "Let's just get this over with..."
    "He puts the book back on his lap, sighs and scratches his neck for a second."
    an "The name's Adam Nord. I hope you feel less inclined to harass me now that you know my name."
    $ an_name = "Adam"
    an "What's yours, then?"
    jump adam_talk_introduce_2

label adam_talk_introduce_2:
    $ player_name = renpy.input("Please enter a name you'd feel happy with for quite some time. Note that it cannot be changed, so spell carefully.")
    menu:
        "\"It's %(player_name)s.\"":
            jump adam_talk_introduce_3
        "\"I'm %(player_name)s. Pleased to meet you.\"":
            $ an_like += 1
            jump adam_talk_introduce_3
        "--Enter a different name--":
            jump adam_talk_introduce_2

label adam_talk_introduce_3:
    nvl clear
    an "%(player_name)s huh."
    an "Well, now that we've come this far. What do you want? Or can I go back to reading yet?"
    menu:
        "\"What is it you're reading, anyway?\"" if d1_adam_discussed_book == False:
            jump adam_talk_reading
        "\"Read this book?\" Hold out Brave New World" if d1_dining_car_book_taken and d1_adam_shown_bnw == False:
            jump adam_talk_bnw
        "\"I feel better already. You go back to reading and we'll talk some more later.\"":
            an "Sure..."
            jump adam_talk_bye
