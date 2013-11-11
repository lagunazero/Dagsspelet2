label day_1_start:

    $ d1_adam_greeted = False
    $ d1_adam_introduced = False
    $ d1_adam_discussed_book = False
    $ d1_adam_shown_bnw = False
    $ d1_adam_ask_conductor = ""
    $ d1_complete = False
    $ d1_compartment_tried_sleep = False
    $ d1_compartment_window_seen = False
    $ d1_compartment_left = False
    $ d1_hallway_seen = False
    $ d1_neighbour_compartment_open = False
    $ d1_neighbour_compartment_seen_lock = False
    $ d1_neighbour_compartment_has_waited = False
    $ d1_neighbour_compartment_has_knocked = False
    $ d1_dining_car_seen = False
    $ d1_dining_car_looked_around = False
    $ d1_dining_car_ordered = False
    $ d1_dining_car_book_left = False
    $ d1_dining_car_book_left = False
    $ d1_dining_car_book_taken = False
    $ d1_searched_conductor = 0

    nvl clear
    "DUB-DUB. DUB-DUB. DUB-DUB." #TODO SFX: Train dub-dub
    "Before opening my eyes, I stretch my arms as far up as I could and slowly rotate my head from left to right. The seat's wood-hard padding hadn't done much to make an already uncomfortable trip - in double meaning - any nicer."
    "Looking upwards, I spot a No Smoking sign half buried beneath layers of dust and dirt. The stuffy air makes me doubt it's ever been adhered to."
    "Taking a deep breath, I can't help but start coughing. It's probably been close to 12 hours since last I ate, and at least half that since the last cup of anything."
    "Should probably do something about that."
    "I clear my throat and am about to spit what little fluid I have left in me before I remember where I am. This trip must be making me dizzy."
    nvl clear
    an "Hrmph."
    #TODO VFX: Open eyes
    "Opposite to me sits a man that my nap had made me forget. Or maybe he hadn't been there before, I'm not sure."
    "He sits with a straight back and folded legs, as though having no problem at all with the lackluster seats. His plain white shirt is tucked neatly into the black pants. Can he have dropped his tie? Or bowtie, maybe."
    "Upon noticing my gaze he raises a wasp-striped book in between our eyes."
    jump menu_train_compartment

label menu_train_compartment:
    if d1_adam_greeted and d1_dining_car_seen and d1_adam_introduced == False and d1_adam_ask_conductor == "":
        jump train_compartment_pa_delay
    else:
        menu:
            "Greet the other passenger" if d1_adam_ask_conductor == "" and d1_adam_introduced == False and an_location == "train_compartment":
                jump adam_greet
            "Talk to the other passenger" if d1_adam_ask_conductor != "" and d1_adam_introduced == False and an_location == "train_compartment":
                if d1_adam_ask_conductor == "agreed":
                    jump adam_search_conductor_agreed
                else:
                    jump adam_search_conductor_refused
            "Talk to Adam" if d1_adam_introduced and an_location == "train_compartment":
                "He slowly takes down the book a few centimeters and looks at me across it."
                an "What is it now?"
                jump menu_adam_talk
            "Try to go back to sleep":
                jump try_sleep
            "Look out the window":
                jump train_compartment_window
            "Go outside":
                jump train_compartment_leave
                
label adam_search_conductor_agreed:
    nvl clear
    an "You found the conductor yet?"
    menu:
        "\"No, I don't think there's anyone around\"":
            me "No, I don't think there's anyone around."
            jump adam_searched_conductor
        "\"No, haven't really looked yet\"":
            me "No, haven't really looked yet."
            an "Then I don't see what you're talking to me."
            "He promptly begins to read again."
            jump menu_train_compartment

label adam_search_conductor_refused:
    nvl clear
    an ".....You've become cooperative yet?"
    menu:
        "\"Fine, I'll search for the conductor\"":
            $ an_like += 1
            $ d1_adam_ask_conductor = "agreed"
            me "Fine, I'll search for the conductor."
            an "Ah!"
            "A row of teeth flashes by for an instant on the man's face, but then it's gone as quickly as it came."
            an "Fantastic."
            "Without a further word the man resumes reading."
            jump menu_train_compartment
        "\"Nope\"":
            me "Nope."
            an "Bah!"
            "The man grunts and returns to his book."
            jump menu_train_compartment
        "\"Actually, there's no conductor around\"":
            an "......"
            an "You've actually looked?"
            menu:
                "\"No, not really\"":
                    me "No, not really."
                    an "Bah!"
                    "The man grunts and returns to his book."
                    jump menu_train_compartment
                "\"Yeah\"":
                    me "Yeah. No conductor around."
                    jump adam_searched_conductor

label train_compartment_window:
    nvl clear
    if d1_compartment_window_seen:
        "I have to squint, if not straight up fantasize, to see any remains of the sun now."
        "Out in the middle of nowhere like this there's not exactly any city light to make up for the lack of a present sun, either, so I'm left in the dark."
        "Which consequently makes it rather dull to view."
    else:
        $ d1_compartment_window_seen = True
        "I move my eyes from my bothered co-passenger and onto the compartment's sole window. Our eyes are amazing enough that focusing on the rapidly moving terrain beyond it means I can't even see the stains."
        "The last rays of the setting sun flashes rapidly between the trees of this continental forest, making me unvolountarily squint just as frequently. I can stand it for at least a short while because of how prettily the deep orange light outlines the tree silhouttes."
        "I try searching for animals for a few minutes, but the best I can come up with is a pile that might have been left there by a deer; but it might just as well be some roots, leaves and mud."
        nvl clear
        "Who knows, maybe I should try getting a career as a naturalist painter. Make a living recreating stuff like this."
        "Well, maybe not the pile of could-be feces."
        "According to the train schedule there's still plenty of time before we reach the next city, not to mention my destination."
        "That gives me plenty of chances to find motives that are more interesting than anything in this compartment."
        #TODO VFX: Flash Adam
        "Not that that should be too difficult."
        nvl clear
        "I finally sigh and turn back from the window. Trees are a nice change from being ignored, but they're not all that much better at responding to what I say or think."
        "...So they're not really all that much of a change."
    jump menu_train_compartment

label adam_greet:
    nvl clear
    #TODO VFX: Show Adam
    if d1_adam_greeted:
        me "Umm, excuse me?"
        an "........"
    else:
        me "Hello?"
        an "........"
        an "Hrm."
    $ d1_adam_greeted = True
    jump menu_train_compartment

label try_sleep:
    nvl clear
    if d1_complete:
        "Finally a moment's peace."
        jump day_1_end
    else:
        if d1_compartment_tried_sleep:
            "Before I even complete leaning against the hard back I know I won't be able to sleep in yet a little while."
            
            "During the few seconds that my eyes were closed, or on their way to being at least, the man across from me has turned another page."
            "Other than that the whole train car seems frozen in time, with only the soft thumping and the dim landscape indicating there's anything at all outside."
        else:
            $ d1_compartment_tried_sleep = True
            "I lean back and shut my eyes again. Hopefully another couple hours' of shuteye will mean I'll wake up with an arrived train."
            "DUB-DUB."
            "DUB-DUB."
            "DUB-DUB."
            "Maybe I'll... No, shut up."
            "DUB-DUB."
            "DUB-DUB."
            nvl clear
            "DUB-DUB."
            "DUB-DUB."
            "So thirsty..."
            "DUB-DUB."
            nvl clear
            "DUB-DUB."
            "DUB-DUB."
            "I try to get into listening mindlessly to the train's steady rolling, but my body's much too awake."
            "I could spend another hour or more sitting like this without getting any closer to sleep. And then what's the point?"
            nvl clear
            "I open my eyes again and look at the man across from me. He's still busy reading his book and ignoring me, unsurprisingly."
        jump menu_train_compartment

label train_compartment_leave:
    nvl clear
    if d1_compartment_left == False:
        $ d1_compartment_left = True
        "I get up from the seat and give it a look that I try to make as hard as its object, then head for the exit."
        "On my way I try to glance at the other passenger but he's doing a very capable job of conveniently placing the book he's reading right between us."
    jump train_hallway

label train_hallway:
    nvl clear
    if d1_hallway_seen:
        "I emerge once more into the train's hallway."
    else:
        $ d1_hallway_seen = True
        "Closing the sliding door behind me I enter a fairly long and quite narrow hallway. There are several compartments on each side of mine, likely about as interesting though perhaps lacking in the Ignoring Man department."
        "Maybe I ought to switch, huh?"
    if d1_adam_ask_conductor == "agreed" and d1_searched_conductor == 0:
        $ d1_searched_conductor += 1
        "I look around for a conductor but the hallway's completely empty, save for myself."
        "Usually I wouldn't be complaining about that, though."
    jump menu_train_hallway

menu menu_train_hallway:
    "Go back to my compartment":
        nvl clear
        "Guess I don't have much to do out here anyway."
        "I step back in and receive a brief, if even that, glance from my co-passenger before he resumes reading."
        jump menu_train_compartment
    "Enter the neighbouring compartment" if d1_neighbour_compartment_seen_lock == False:
        jump neighbour_compartment_locked
    "Knock on the neighbouring compartment" if d1_neighbour_compartment_seen_lock == True:
        jump neighbour_compartment_knock
    "Go to the dining car":
        jump dining_car

label neighbour_compartment_knock:
    nvl clear
    #TODO SFX: 3 knocks
    "Knock, knock, knock."
    "I give the door three rapid taps and listen for a reaction."
    "A second passes..."
    "Another one..."
    "Another one..."
    menu menu_neighbour_compartment:
        "Knock again" if d1_neighbour_compartment_has_knocked == False:
            jump neighbour_compartment_knock_again
        "Wait some more" if d1_neighbour_compartment_has_waited == False:
            jump neighbour_compartment_knock_wait
        "Give it up":
            jump neighbour_compartment_knock_give_up

label neighbour_compartment_knock_again:
    $ d1_neighbour_compartment_has_knocked = True
    nvl clear
    "I give it one more go, this time knocking a bit harder."
    #TODO SFX: 3 strong knocks
    "KNOCK, KNOCK, KNOCK."
    "..."
    "..........."
    "............................."
    "Still no response."
    jump menu_neighbour_compartment
    
label neighbour_compartment_knock_wait:
    $ d1_neighbour_compartment_has_waited = True
    nvl clear
    "I'll show some patience. Maybe whoever's in there was asleep, like I was."
    "Or... maybe that person is an ignoring snob, like a certain someone else..."
    nvl clear
    "Regardless, waiting provokes no further response and it becomes evidently clear that there's no point in sticking around in silence longer than I already have."
    menu:
        "Try knocking instead" if d1_neighbour_compartment_has_knocked == False:
            jump neighbour_compartment_knock_again
        "Give it up":
            jump neighbour_compartment_knock_give_up

label neighbour_compartment_knock_give_up:
    nvl clear
    "It's not like I had a particularly good reason for getting in there to begin with, so it's not really worth making too much of a fuss over."
    "But failing, no matter the subject, is never apppealing."
    if d1_neighbour_compartment_has_knocked:
        "Plus, this whole knocking thing must have made me look tremendously stupid to all the zero spectators."
    "I turn around and give the empty train hallway another good look."
    "It's still got just the same options as before. Unless I'm counting stupid things like hanging around locked doors."
    jump menu_train_hallway

label neighbour_compartment_locked:
    nvl clear
    $ d1_neighbour_compartment_seen_lock = True
    "I'll see what's in the compartment next door. Maybe I can stay there in isolation."
    "I don't have any cargo with me anyway, so I'm not really tied to my given seat. At least as long as no conductor makes a hassle, that is."
    "I place my hand in the sliding door's small socket and pull softly."
    #TODO SFX: Locked door
    "It's locked!"
    nvl clear
    "Having tried this, I can still make my hardest to fool myself into retroactively having expected this. It's not like they'll want people wandering around."
    "Then again, it's not like my compartment was locked. Or maybe I just didn't lock it..."
    jump menu_train_hallway

label dining_car:
    if d1_dining_car_seen:
        jump dining_car_2
    else:
        jump dining_car_1
        
label dining_car_1:
    $ d1_dining_car_seen = True
    nvl clear
    "I leave the dull hallway and head for the dining car. I'm not particularly hungry, but at least it'll give me something to do."
    nvl clear
    "Just entering the dining car I'm assaulted by a thick smell of fried butter and red wine. There's an accompanying sheet of smoke pouring out from the door to the shut-off kitchen. Shouldn't the fire alarm be panicking right about now?"
    "From behind the kitchen door I can hear laughter and boisterous cheering, interspersed with clanking of glasses."
    "The car itself is spacious, mostly because there aren't any other passengers present."
    if d1_adam_ask_conductor == "agreed" and d1_searched_conductor == 1:
        $ d1_searched_conductor += 1
        "While there might be a conductor or two in the kitchen, I get the feeling no-one there would be of any help."
    menu menu_dining_car:
        "Look around" if d1_dining_car_looked_around == False:
            jump dining_car_look
        "Try to make an order" if d1_dining_car_ordered == False:
            jump dining_car_order
        "Take the book" if d1_dining_car_book_left == True and d1_dining_car_book_taken == False:
            "I return to the table where I put back the forgotten book and pick it up."
            jump dining_car_book_take
        "Head back to the hallway":
            nvl clear
            "Not much else to do here."
            jump menu_train_hallway

label dining_car_2:
    nvl clear
    "I return to the dining car. It's still empty, aside from the formidable wall of smoke emitted from the kitchen. I can still hear rowdy voices from inside."
    if d1_adam_ask_conductor == "agreed" and d1_searched_conductor == 1:
        $ d1_searched_conductor += 1
        "While there might be a conductor or two in the kitchen, I get the feeling no-one there would be of any help."
    jump menu_dining_car

label dining_car_look:
    $ d1_dining_car_looked_around = True
    nvl clear
    "I ignore the smoking kitchen and take a look around the deserted dining area instead."
    "There are about a dozen small tables in all, with chair shoe-horned into whatever free space there is. How anyone can pass through here when it's full of people?"
    "The interior's fancy decor - some satin here and some mahogany there - is not enough to hide that the whole place is closer to a freeway lunch bar than the \"World Cuisine in a 100-Wheeled Palace\" that's promised on an old poster by the entrance. There's hardly a chair whose seat isn't showing its filling or a table without greasy stains and scratches deeper than a dining knife could cause."
    nvl clear
    "Strolling around the empty car with a slightly disdainful, but not really caring, look on my face I spot a fairly thin, gray book on the floor underneath a corner table."
    "I reach down and pick it up, wiping away some food crusts."
    "Aldous Huxley, Brave New World."
    "The cover shows a disconcerting close-up of a white face with wide-open eyes."
    menu:
        "Pocket it":
            jump dining_car_book_take
        "Leave it":
            jump dining_car_book_leave
    
label dining_car_book_take:
    $ d1_dining_car_book_taken = True
    nvl clear
    "Regardless of whether I want it or not, it should at least help me pass the time."
    "I don't think I feel like sitting around here reading it, though. The owner might show up."
    "While the situation more or less validates finders keepers I'd prefer to avoid the fight."
    jump menu_dining_car

label dining_car_book_leave:
    $ d1_dining_car_book_left = True
    nvl clear
    "I decide not to take it, putting it back on top of the table under which it had been. At least that's a slightly more dignified place to be."
    jump menu_dining_car

label dining_car_order:
    $ d1_dining_car_ordered = True
    nvl clear
    "I pick a table at random and take a seat. Glancing over the menu it seems they don't intend for economic class passengers like me to eat here."
    "Maybe I can at least get one of the starters and something to drink. My throat's killing me and, given half a moment's attention, my stomach seems to be in a similar condition."
    menu:
        "Pick Caviar Canapés":
            jump dining_car_order_2
        "Pick Beet Salad":
            jump dining_car_order_2
        "Pick Lobster Bisque":
            jump dining_car_order_2
        "Pick Caesar Salad":
            jump dining_car_order_2

label dining_car_order_2:
    nvl clear
    "I look around to see if there's any waiter around, but no such luck."
    "Clearing my throat loudly causes no visible reaction."
    nvl clear
    "I try knocking hard on the table..."
    #TODO SFX: table knocking
    "...but still nothing."
    nvl clear
    me "Anyone there?"
    me "I'd kind of like to take an order...?"
    "At first it's silent for a second, but then another rumbustious cheering erupts from the other side and I'm forced to admit that I likely wasn't heard."
    "Hopefully."
    nvl clear
    "I get up from the chair with a sigh."
    "If the personnel is this engaged with the table waiting my hopes sink pretty low with regards to the served food. Maybe I'll have more luck tomorrow."
    "My stomach will at least force me to be a lot more insistent."
    jump menu_dining_car

label train_compartment_pa_delay:
    nvl clear
    #TODO SFX: pa buzz
    "As I lean back against the seat's barely stuffed back, the PA system comes on with a crackling buzz."
    pa "*bzzt* *crackle-bzzt* ..that bitch should take her trashy ass outta here. I mean, seriously, what's..."
    pa ".........."
    pa "What's that? It is?!"
    #TODO SFX: pa buzz
    pa "*bzzt-bzzt*"
    "The PA buzzes off again."
    nvl clear
    "I might be imagining it, but I could swear the man opposite me has tightened his grip on the book he's holding."
    "A bit more aware of my surroundings, I hear that the dub-dub-dub from the tracks are coming with longer intervals and the dusky trees outside the window are passing by at a lower speed."
    "After rolling my thumbs for another ten seconds the PA system comes back online, though I can probably guess what they're going to say."
    #TODO SFX: pa buzz
    pa "*crackle-crackle-bzzt* Umm, right..."
    pa "We're sorry to say that we're forced to slow down for a while."
    pa "No, wait. We'll actually stop shortly."
    pa "All the staff aboard are very sorry for this inconvenience. We'll notify you as soon as we know more."
    pa "*bzzt-bzzt*"
    nvl clear
    "The PA goes silent once more, but for the train compartment it doesn't last long."
    an "But WHY?!"
    "The man opposite me rushes to his feet and glares menacingly at the PA speaker, holding his book like a club; though an impractical one."
    menu:
        "Sit silent":
            jump adam_pa_delay_silent
        "Inquire":
            jump adam_pa_delay_inquire

label adam_pa_delay_silent:
    nvl clear
    "The man wiggles the book back and forth, his face still flushed. After a few seconds of wheezing, he lets out a deep sigh and sits down again."
    "He wipes some sweat from his brow and adjusts his glasses, then lets his fingers remain pinched against his nose and shuts his eyes."
    nvl clear
    "When he opens them back again he catches me observing him."
    an "Ehm..."
    an "Hrmm."
    "He starts to put the book back up, but only gets it half-way before he sighs and puts it on the table between us instead."
    jump adam_pa_delay_talk
    
label adam_pa_delay_inquire:
    nvl clear
    me "So..."
    "The man jerks back into the seat at the sound of my voice, nearly dropping his glasses on the way."
    "He fumbles with them for a few seconds before he manages to secure them, after which he places the book on the table and turns to me."
    "His face is flushed red."
    an "Well, hrmm."
    jump adam_pa_delay_talk

label adam_pa_delay_talk:
    nvl clear
    an "Why are we stopping? What's the cause for it?"
    me "Haven't the foggiest. Sorry..."
    "I hold out my hands in a gesture that I hope he takes as something quite the same as what I said."
    nvl clear
    "He scratches his forehead and brushes a curl away from his eyes; which have taken on a quite apologetic character."
    an "I know you don't know, you know."
    an "What I meant was: Why didn't they TELL us why we're stopping instead of just stating the obvious."
    an "As if we're not late enough already...!"
    jump adam_pa_delay_how_late
#    menu:
#        "\"How late are we?\"":
#            jump adam_pa_delay_how_late
#        "\"You're in a hurry?\"":
#            jump adam_pa_delay_ask_hurry
#        "\"Chill, man\"":
#            jump adam_pa_delay_chill

label adam_pa_delay_how_late:
    nvl clear
    me "How late are we?"
    "For some reason I get an annoyed look in response."
    me "...See, I've been going for so long now that I'm not really keeping track anymore."
    "The man gives me a long look, then grunts lightly."
    an "We were SUPPOSED to arrive yesterday. But I imagine it's hard to keep track of time when you waste it all with sleep."
    me "Oh."
    me "At least you've got a book to read. You seem pretty into it."
    an "Hah!"
    nvl clear
    an "I'm so into it that I've read it back to back three times now."
    me "Sounds like it's a good---"
    an "On this trip!"
    "The man strikes out with his hands in the air and sighs dramatically."
    an "If only I'd find some worth in something mundane, like sleep... But instead I'm learning this book phrase by phrase."
    nvl clear
    an "Say..."
    an "Why don't you hurry off to find a conductor?"
    an "Get someone to make an attempt at explaining the reason for this hold-up."
    menu:
        "\"Well, alright then\"":
            $ d1_adam_ask_conductor = "agreed"
            $ an_like += 2
            nvl clear
            me "Well, alright then."
            "The man blinks, then straightens up and picks his book up."
            "After a stern nod at me, and something that might be interpreted as a smile, he resumes reading again."
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
                "\"I'm not that interested\"":
                    $ d1_adam_ask_conductor = "refused"
                    $ an_like -= 2
                    nvl clear
                    me "I'm not that interested."
                    an ".........."
                    an "Fine."
                    an "Fine!"
                    "The man picks up his book again violently and resumes reading."
                    jump menu_train_compartment

label adam_searched_conductor:
    nvl clear
    if d1_searched_conductor > 0:
        $ an_like += 1
        an "Hmm, that's certainly a shame."
        an "Though not a surprising one, given the ineptitude of the train personnel."
        "He rolls his eyes and sighs heavily."
        jump adam_after_searched_conductor
    else:
        $ an_like -= 3
        an "Don't take me for a fool!"
        "His fingers clench the book tightly and at least a few veins on his forehead pop."
        an "You've just been sitting right where you are!"
        an "You think you're some kind of Twain character?! Bah!"
        "He picks his book back up before I have a chance to retort, but his hands are still shaking so much that I doubt anyone could read it right now."
        nvl clear
        "While I'm not keen on running his errands, I feel bad for making him so upset."
        "I think he might be crying a little, actually."
        me "Ehm... I'm sorry?"
        "He responds with nothing but an angry sniffle."
        nvl clear
        "......"
        "............"
        "........................"
        "................................................"
        "An awkward minute passes."
        nvl clear
        me "I, ehh, I can go look for a conductor..?"
        an "...........Hrm."
        "Without bringing the book down from between us, he sniffles a few times and then clears his throat."
        an "No."
        an "No, it's quite alright."
        me "But---"
        an "Given the aptitude of the staff, there probably wouldn't have been much information to be gained regardless."
        jump adam_after_searched_conductor

label adam_after_searched_conductor:
    nvl clear
    an "I don't see much use in expending any further efforts on this matter."
    an "For either of us."
    "He is about to, yet again, return to his book when he pauses and looks up at me."
    "His lips tighten and his gaze locks onto mine."
    "It feels like he's really looking at me for the first time, and I hesitate to pull back."
    "Whatever his game is, I'm not about to piss him off right now."
    "That said, his gaze is an unconvincing mix of menace, analysis and general bewilderment that's quite a bit discomforting to meet straight on."
    "Not that I'm going to stop that from making this a proper stare contest, if that's what he wants!"
    nvl clear
    "He suddenly relaxes his intense observation of me."
    an "The name is Adam Nord."
    $ an_name = "Adam"
    if an_like < 0:
        an "It's my hope you'll feel less inclined to harass me now that you know my name."
    "I reach out my hand and he hesitantly shakes it."
    me "I'm Kim. Kim Erling."
    nvl clear
    an "Just like Kipling's, eh..."
    "Adam mutters beneath his breath."
    an "Well! That's another matter settled and done with."
    "He smiles to himself and looks ready to ignore me again, but then meets my eyes once more."
    an "Or was there something else?"
    jump menu_adam_talk

menu menu_adam_talk:
    "\"What is it you're reading, anyway?\"" if d1_adam_discussed_book == False:
        $ d1_adam_introduced = True
        jump adam_talk_reading
    "\"Read this book?\" Hold out Brave New World" if d1_dining_car_book_taken and d1_adam_shown_bnw == False:
        $ d1_adam_introduced = True
        jump adam_talk_bnw
    "\"No, not really\"":
        if d1_adam_introduced == False:
            $ d1_adam_introduced = True
            jump adam_talk_bye
        else:
            an "Hrm."
            "He resumes reading with an annoyed expression."
            jump menu_train_compartment

label adam_talk_bye:
    nvl clear
    "Adam brings the book back up between us, but there's less hostility in the action now. Or maybe I'm just imagining things. It's not like I made the best of impressions on him."
    "But at least we're now on a name-knowing basis which, seeing how we're likely to spend at least a dozen more hours together, is a decent first step to having a less isolated trip."
    jump menu_train_compartment

#TODO content
label adam_talk_reading:
    $ an_like += 2
    $ d1_adam_discussed_book = True
    nvl clear

#TODO content
label adam_talk_bnw:
    $ an_like += 2
    $ d1_adam_shown_bnw = True
    nvl clear

#TODO content
label day_1_end:
    return
