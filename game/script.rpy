transform photo_pos:
    xalign 0.25 yalign 0.42 zoom 0.45

label start:
    $ save_name = "BOOT UP"
    scene bg samsara

    $ quick_menu = False

    if persistent.completed:
        "THIS INTAKE HAS BEEN COMPLETED."
        "WELCOME BACK, [persistent.player_name]"
        "PROCEED?"
        menu:
            "proceed":
                pass


    "Welcome to Samsara Staffing Services."
    "You are about to begin a short survey so we can get a better understanding of who you are."
    "Answer each question as truthfully as possible."
    "The survey will begin momentarily."

# phase 1: boring
label question_1:
    $ save_name = "QUESTION 1"
    show screen hud
    $ ask(1)
    "Question [qnum]. What is your preferred name?"
    $ persistent.player_name = renpy.input("Type your name here.", length=32).strip() or "New Employee"
    $ record(persistent.player_name, typed=True)

label question_2:
    $ save_name = "QUESTION 2"
    $ ask(2)
    "Question [qnum]. How did you hear about us?"
    menu:
        "referral":
            $ record("referral")
        "previous employer":
            $ record("previous employer")
        "academic supervisor":
            $ record("academic supervisor")
        "written correspondence":
            $ record("written correspondence")
        "you were listed":
            $ record("listed")

label question_3:
    $ save_name = "QUESTION 3"
    $ ask(3)
    "Question [qnum]. What are the best days to reach you?"
    $ player_day = renpy.input("Enter which days you are available.", length=32).strip() or "a weekday"
    $ record(player_day, typed=True)

label question_4:
    $ save_name = "QUESTION 4"
    $ ask(4)
    "Question [qnum]. What are the best times to reach you?"
    $ player_time = renpy.input("Enter which times you are available.", length=32).strip() or "a convenient time"
    $ record(player_time, typed=True)

label question_5:
    $ save_name = "QUESTION 5"
    $ ask(5)
    "Question [qnum]. Have you had any previous employers?"
    menu:
        "municipal government":
            $ record("municipal")
        "private research":
            $ record("private research")
        "academic institution":
            $ record("academic")
        "Royce Technologies":
            $ record("royce")
            "..."
        "none of the above":
            $ record("none")

label question_6:
    $ save_name = "QUESTION 6"
    $ ask(6)
    "Question [qnum]. Do you object to working in a facility that predates its records?"
    menu:
        "yes":
            $ record("yes")
        "no":
            $ record("no")
        "unsure":
            $ record("unsure")

label question_7:
    $ save_name = "QUESTION 7"
    $ ask(7)
    "Question [qnum]. If something happened to you, who would be first to notice your absence?"
    $ player_contact = renpy.input("Enter the name of your emergency contact.", length=32).strip() or "no one listed"
    $ record(player_contact, typed=True)

label question_8:
    $ save_name = "QUESTION 8"
    $ ask(8)
    "Question [qnum]. How long would it take them to notice?"
    menu:
        "immediately":
            $ record("immediately")
        "within a day":
            $ record("a day")
        "within a week":
            $ record("a week")
        "longer":
            $ record("longer")

# phase 2: ethics    
label question_9:
    $ save_name = "QUE$T1ON 9"
    $ ask(9)
    "Question [qnum]. Two coworkers submit accounts of the same event. The accounts contradict each other. Neither coworker is known to be reliable."
    menu:
        "determine which account is correct":
            $ record("determine", lean="fear")
        "interview both again":
            $ record("interview", lean="respect")
        "file both accounts":
            $ record("file")
        "defer to the senior coworker":
            $ record("defer", lean="fear")
        "(go back)":
            $ revise(9)
            jump question_9

label question_10:
    $ save_name = "QUESTION 10"
    $ ask(10)
    "Question [qnum]. An object in your care is requested by the person it was taken from. The request is not authorized."
    menu:
        "deny the request":
            $ record("deny", lean="fear")
        "escalate it":
            $ record("escalate")
        "return the object":
            $ record("return", lean="respect")
        "ask why it was taken":
            $ record("ask why", lean="respect")

label question_11:
    $ save_name = "Q█EST█ON █1"
    $ set_title("█████ ████████████")
    $ skin = "royce"
    scene bg royce
    $ ask(11)
    "Question [qnum]. Are the people in this photo familiar?"
    # royce family photo
    show royce_family at photo_pos
    menu:
        "yes":
            $ record("yes")
        "no":
            $ record("no")
        "unsure":
            $ record("unsure")
        "I was not shown a photo":
            $ record("denied the photo")
    hide royce_family

label question_12:
    $ save_name = "QUESTION 12"
    $ ask(12)
    "Question [qnum]. You are observing something. Continued observation will change it."
    menu:
        "continue observing":
            $ record("continue", lean="fear")
        "stop":
            $ record("stop", lean="respect")
        "record what is changing":
            $ record("record")
        "predict what it is changing into":
            $ record("predict", lean="fear")

label question_13:
    $ save_name = "QUESTION 13"
    $ ask(13)
    "Question [qnum]. A superior instructs you to discard a witness report."
    menu:
        "discard it":
            $ record("discard", lean="fear")
        "discard it and note the instruction":
            $ record("note", lean="respect")
        "refuse":
            $ record("refuse", lean="respect")
        "keep a copy":
            $ record("copy", lean="fear")
        
# phase 3: council
label question_14:
    $ save_name = "████████ ██"
    $ ask(14)
    "Question [qnum]. Has anyone ever wronged you?"
    menu:
        "yes":
            $ record("yes")
        "no":
            $ record("no")

label question_15:
    $ save_name = "██████ █"
    $ ask(15)
    "Question [qnum]. If justice were impossible, would revenge be enough?"
label question_15_menu:
    menu:
        set q15_removed
        "yes":
            # breathing sounds play as you hover over this option
            $ record("yes", lean="fear")
            if "no" in q15_removed:
                "Thank you for correcting your previous answer."
        "no":
            $ record("no (not accepted)", lean="respect")
            "INCORRECT."
            "THAT ANSWER IS NOT AVAILABLE."
            "TRY AGAIN."
            jump question_15_menu

label question_16:
    $ save_name = "██ ██ ███"
    $ ask(16)
    "Have you seen a god?"
    menu:
        "yes":
            $ record("yes")
        "no":
            $ record("no")
        "unsure":
            $ record("unsure")

label question_17:
    $ save_name = "████"
    $ ask(17)
    "Would you like to?"
    menu:
        "yes":
            $ record("yes")
        "no":
            $ record("no")
        # The god is shown anyway, a hazy, glowing, low-poly model in a black void. The image is blurred, and the player can't entirely see it. The droning background noise cuts out just for this moment.
    $ drone(False)
    hide screen hud
    scene black
    show god_blur
    $ renpy.pause(4.0, hard=True)
    scene bg royce
    show screen hud
    $ drone(True)

label question_18:
    $ save_name = "QUESTION 18"
    $ ask(18)
    $ mins = elapsed_minutes()
    "Question [qnum]. This form has been open for [mins] minutes. Is that longer than you intended?"
    menu:
        "yes":
            $ record("yes")
        "no":
            $ record("no")
        "I was not counting":
            $ record("not counting")

label question_19:
    $ save_name = "QUESTION 19"
    $ ask(19)
    "Question [qnum]. Is this the first time you have completed this assessment?"
    menu:
        "yes":
            $ record("yes" if persistent.completed else "yes (false)")
        "no":
            $ record("no" if not persistent.completed else "no (false)")
        "unsure":
            $ record("unsure")

label question_20:
    $ import datetime
    $ now = datetime.datetime.now()
    $ clock, today = now.strftime("%I:%M %p").lstrip("0"), now.strftime("%A")
    $ ask(20)
    "Question [qnum]. It is [clock]. You said the best days to reach you were [player_day]. Today is [today]."
    "Is anyone else in the room with you?"

label question_21:
    hide screen hud
    call screen freeze("RETRIEVING FILE")
    show screen hud
    $ set_title("COUNCIL")
    $ skin = "council"
    scene bg council
    $ save_name = "HELD"
    $ ask(21)
    "Question [qnum]. How long has the council been aware of you?"
    menu:
        "since I applied":
            $ record("since applied")
        "longer":
            $ record("longer")
        "I would not know":
            $ record("would not know")

# phase 4: meta
label question_22:
    $ save_name = "QUESTION 22"
    $ ask(22)
    $ lq = longest_q()
    "Question [qnum]. Question [lq] took you longer than the others. What caused that?"
    menu: 
        "I was thinking":
            $ record("thinking")
        "I was unsure":
            $ record("unsure")
        "I did not understand the question":
            $ record("did not understand")
        "I don't recall hesitating":
            $ record("don't recall")
    $ qtotal = 24
    if revisions:
        jump question_23
    else:
        jump question_24

    
label question_23:
    $ save_name = "QUESTION 23"
    $ ask(23)
    "Question [qnum]. You changed your answer to question [revised_q]. What caused that?"
    $ player_revision = renpy.input("", length=60).strip() or "(no answer)"
    $ record(player_revision, typed=True)
    jump question_24

label question_24:
    $ save_name = "QUESTION 24"
    $ ask(24)
    "Question [qnum]. You have not revised any answer."
    menu:
        "I was certain":
            $ record("certain")
        "I did not consider it":
            $ record("did not consider")
        "revising did not occur to me":
            $ record("did not occur")

label question_25:
    $ save_name = "QUESTION 25"
    $ ask(25)
    "Question [qnum]. Does this intake require a ninth reading?"
    menu:
        "yes":
            $ record("yes")
        "no":
            $ record("no")
        "this question was not addressed to me":
            $ record("not addressed")
    
label question_26:
    $ save_name = ""
    $ ask(26)
    window hide
    menu:
        "I accept what has happened.":
            $ record("accept")
        "I do not accept what has happened.":
            $ record("did not accept")

# end
label intake_end:
    $ persistent.completed = True
    $ save_cross_game()
    window show
    "Thank you for your participation. Your file has been forwarded."
    hide screen hud
    window hide
    call screen intake_result
    window auto
    scene black
    "WE WILL CONTACT YOU ON [player_day!u] AT [player_time!u]."
    $ renpy.quit()