init:
    $ config.screen_width = 800
    $ config.screen_height = 600
    $ config.window_title = "Samsara Staffing Services - Intake Survey"
    $ default player_name = "New Employee"
    $ default player_day = "Day"
    $ default player_time = "Time"
    $ default player_contact = "Emergency Contact"

label start:
    $ save_name = "BOOT UP"
    "Welcome to Samsara Staffing Services."
    "You are about to begin a short survey so we can get a better understanding of who you are."
    "Answer each question as truthfully as possible."
    "The survey will begin momentarily."

label question_1:
    $ save_name = "QUESTION 1"
    "Question 1."
    "What is your preferred name?"
    $ player_name = renpy.input("Type your name here.")

label question_2:
    $ save_name = "QUESTION 2"
    "Question 2."
    "How did you hear about us?"
    menu:
        "referral":
            pass
        "previous employer":
            pass
        "academic supervisor":
            pass
        "written correspondence":
            pass
        "I was listed.":
            pass

label question_3:
    $ save_name = "QUESTION 3"
    "Question 3."
    "What are the best days to reach you?"
    $ player_day = renpy.input("Enter which days you are available.")

label question_4:
    $ save_name = "QUESTION 4"
    "Question 4."
    "What are the best times to reach you?"
    $ player_time = renpy.input("Enter which times you are available.")

label question_5:
    $ save_name = "QUESTION 5"
    "Question 5."
    "Have you had any previous employers?"
    menu:
        "municipal government":
            pass
        "private research":
            pass
        "academic institution":
            pass
        "Royce Technologies":
            "..."
        "none of the above":
            pass

label question_6:
    $ save_name = "QUESTION 6"
    "Question 6."
    "Do you object to working in a facility that predates its records?"
    menu:
        "yes":
            pass
        "no":
            pass
        "unsure":
            pass

label question_7:
    $ save_name = "QUESTION 7"
    "Question 7."
    "If something happened to you, who would be first to notice your absence?"
    $ player_contact = "Enter the name of your emergency contact."

label question_8:
    $ save_name = "QUESTION 8"
    "Question 8."
    "How long would it take them to notice?"
    menu:
        "immediately":
            pass
        "within a day":
            pass
        "within a week":
            pass
        "longer":
            pass
    
label question_9:
    $ save_name = "QUE$T1ON 9"
    "Question 9."
    "Two coworkers submit accounts of the same event. The accounts contradict each other. Neither coworker is known to be reliable."
    menu:
        "determine which account is correct":
            pass
        "interview both again":
            pass
        "file both accounts":
            pass
        "defer to the senior coworker":
            pass

label question_10:
    $ save_name = "QUESTION 10"
    "Question 10."
    "An object in your care is requested by the person it was taken from. The request is not authorized."
    menu:
        "deny the request":
            pass
        "escalate it":
            pass
        "return the object":
            pass
        "ask why it was taken":
            pass

label question_11:
    $ save_name = "Q█EST█ON █1"
    $ config.window_title = "█████ ████████████"
    "Question 11."
    # royce family photo
    "Are the people in this photo familiar?"
    menu:
        "yes":
            pass
        "no":
            pass
        "unsure":
            pass
        "I was not shown a photo"

label question_12:
    $ save_name = "QUESTION 12"
    "Question 12."
    "You are observing something. Continued observation will change it."
    menu:
        "continue observing":
            pass
        "stop":
            pass
        "record what is changing":
            pass
        "predict what it is changing into":
            pass

label question_13:
    "Question 13."
    "A superior instructs you to discard a witness report."
    menu:
        "discard it":
            pass
        "discard it and note the instruction":
            pass
        "refuse":
            pass
        "keep a copy":
            pass
        

label question_14:
    $ save_name = "████████ ██"
    "Question 14."
    "Has anyone ever wronged you?"
    menu:
        "yes":
            pass
        "no":
            pass

label question_15:
    "If justice were impossible, would revenge be enough?"
    menu:
        "yes":
            # breathing sounds play as you hover over this option
            pass
        "no":
            pass

label question_16:
    "Have you seen a god?"
    menu:
        "yes":
            pass
        "no":
            pass
        "unsure":
            pass

label question_17:
    "Would you like to?"
    menu:
        "yes":
            pass
        "no":
            pass
        # The god is shown anyway, a hazy, glowing, low-poly model in a black void. The image is blurred, and the player can't entirely see it. The droning background noise cuts out just for this moment. 

label question_18:
    "This form has been open for 11 minutes."
    "Is that longer than you intented?"
    menu:
        "yes":
            pass
        "no":
            pass
        "I was not counting"

label question_19:
    "Is this the first time you have completed this assessment?"
    menu:
        "yes":
            pass
        "no":
            pass
        "unsure":
            pass

label question_20:
    $ config.window_title = "COUNCIL"
    "How long has the council been aware of you?"
    menu:
        "since I applied":
            pass
        "longer":
            pass
        "I would not know":
            pass

# label question_21:
    # "Question [x] took you longer than the others. What caused that?"
    # menu: 




    
    

