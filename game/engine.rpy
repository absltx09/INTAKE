# Settings
define config.window_title = "Samsara Staffing Services - Intake Survey"
define config.rollback_enabled = False
define config.has_sound = False
define config.has_music = False
define config.has_voice = False

define SANS = "DejaVuSans.ttf"
define MONO = "fonts/mono.ttf" if renpy.loadable("fonts/mono.ttf") else "DejaVuSans.ttf"

image royce_family = Placeholder("bg", text="ROYCE FAMILY PHOTO")
image god_blur = Placeholder("bg", text="")

# State
default player_name = "New Employee"
default player_day = "Day"
default player_time = "Time"
default player_contact = "Emergency Contact"
default player_revision = ""

default skin = "samsara" # samsara -> royce -> council
default title_now = "Samsara Staffing Services - Intake Survey"

default log = []
default tally = {"fear": 0, "respect": 0}
default revisions = 0
default revised_q = 0
default confidence = 12
default qnum = 0
default qtotal = 25
default q_label = 0
default t0 = 0.0
default q15_removed = set()

default persistent.completed = False

# recording questions
init python:
    import math

    def ask(n):
        store.q_label = n
        store.qnum += 1
        store.t0 = renpy.get_game_runtime()
    
    def record(answer, lean=None, typed=False):
        dt = round(renpy.get_game_runtime() - store.t0, 1)
        store.log.append({"q": store.q_label, "n": store.qnum, "answer": answer, "lean": lean, "seconds": dt})
        if lean:
            store.tally[lean] += 1
        store.confidence = min (97, store.confidence + (5 if typed else 3))

    def revise(n):
        store.revisions += 1
        store.revised_q = store.qnum
        store.qnum -= 1
        store.confidence = min(97, store.confidence + 6)

    def elapsed_text():
        s = int(renpy.get_game_runtime())
        return "%02d:%02d" % (s // 60, s % 60)

    def elapsed_minutes():
        return max(1, int(renpy.get_game_runtime() // 60))

    def mean_response():
        if not store.log:
            return "--"
        return "%.1fs" % (sum(e["seconds"] for e in store.log) / len(store.log))

    def longest_q():
        if not store.log:
            return 0
        return max(store.log, key=lambda e: e["seconds"])["n"]

    def predicted():
        return "COERCIVE" if store.tally["fear"] > store.tally["respect"] else "CONSENSUAL"

    def set_title(t):
        store.title_now = t
        # config.window_title = t

    def sfx(path, channel="sound"):
        if renpy.loadable(path):
            renpy.play(path, channel=channel)

    def drone(on):
        renpy.music.set_pause(not on, channel="music")

    def save_cross_game():
        mp.predicted = "fear" if store.tally["fear"] > store.tally["respect"] else "respect"
        mp.contact = (store.player_day, store.player_time)
        mp.name = store.player_name
        mp.save()

    mp = MultiPersistent("abslt.registry") 

label after_load:
    $ config.window_title = title_now
    return

# UI skins
# samsara
style samsara_vbox is vbox:
    spacing 6
style samsara_button is button:
    background "#efece4"
    hover_background "#dcd6c8"
    padding (18, 9)
    xsize 400
style samsara_button_text is button_text:
    font SANS
    size 17
    color "#2b2b2b"
    hover_color "#000000"

# royce
style royce_vbox is vbox:
    spacing 4
style royce_button is button:
    background Solid("#120d06")
    hover_background Solid("#3a2a0c")
    padding (14, 7)
    xsize 460
style royce_button_text is button_text:
    font MONO
    size 16
    color "#d9a441"
    hover_color "#ffd72a"

# council
style council_vbox is vbox:
    spacing 10
style council_button is button:
    background None
    hover_background Solid("#1e1c1a")
    padding (14, 7)
    xsize 460
style council_button_text is button_text:
    font MONO
    size 16
    color "#c9c6bf"
    hover_color "#f9e8ac"

# Choice screen
screen choice(items):
    style_prefix skin
    vbox:
        xalign 0.08
        yalign 0.62
        for i in items:
            $ breath = i.kwargs.get("breath", False) 
            textbutton i.caption:
                action i.action
                hovered (Function(sfx, "audio/breath.ogg") if breath else None)
                unhovered (Stop("sound") if breath else None)

# Status column
screen hud():
    zorder 50
    timer 1.0 repeat True action Function(renpy.restart_interaction)

    $ dim = (skin == "council")
    $ ink = {"samsara": "#2b2b2b", "royce": "#d9a441", "council": "#c9c6bf"}[skin]
    $ fnt = SANS if skin == "samsara" else MONO
    $ el, mr, lq = elapsed_text(), mean_response(), longest_q()
    $ header = {"samsara": "SAMSARA STAFFING SERVICES  ·  CANDIDATE ONBOARDING",
                "royce": "RT//NODE 07 · INTAKE SUBSYSTEM",
                "council": "HELD"}[skin]
    
    text header font fnt size 13 color ink xalign 1.0 xoffset -24 ypos 18
    text "QUESTION [qnum] / [qtotal]" font fnt size 13 color ink xalign 1.0 xoffset -24 ypos 38

    vbox: 
        xpos 560 ypos 70 spacing 6
        text "ELAPSED        [el]" font fnt size 12 color ink
        text "REVISIONS      [revisions]" font fnt size 12 color ink
        text "MEAN RESPONSE  [mr]" font fnt size 12 color ink
        text "LONGEST ITEM   [lq]" font fnt size 12 color ink
        null height 10
        text "OBSERVATION CONFIDENCE" font fnt size 12 color ink
        bar value StaticValue(confidence, 100) xsize 200 ysize 8 left_bar Solid(ink if not dim else "#4a4844") right_bar Solid("#00000022")
        if dim:
            text "INSTRUMENT INHERITED.\nNOT RECALIBRATED." font fnt size 10 color "#6e6a64"
            text "REVIEWED ________" font fnt size 10 color "#6e6a64"
        null height 10
        text "NO ERROR" font fnt size 11 color ink

# backgrounds
image bg samsara = Solid("#f6f4ee")
image bg royce = Solid("#0b0805")
image bg council = Solid("#151413")

# Freeze
screen freeze(msg="LOADING"):
    modal True
    zorder 100
    timer t action Return()
    text msg font MONO size 14 color "#d9a441" align (0.5, 0.95)

# results output
screen intake_result():
    modal True
    $ mr, pm = mean_response(), predicted()
    add Solid("#151413")
    vbox:
        xpos 60 ypos 40 spacing 8
        text "CANDIDATE FILE" font MONO size 13 color "#6e6a64"
        text "[player_name!u]" font MONO size 30 color "#f9e8ac"
        null height 8
        text "CONTACT ........... [player_day!u] / [player_time!u]" font MONO size 13 color "#c9c6bf"
        text "NOTIFY ............ [player_contact!u]" font MONO size 13 color "#c9c6bf"
        text "ITEMS ............. [qnum] / [qtotal]" font MONO size 13 color "#c9c6bf"
        text "REVISIONS ......... [revisions]" font MONO size 13 color "#c9c6bf"
        text "MEAN RESPONSE ..... [mr]" font MONO size 13 color "#c9c6bf"
        text "PREDICTED METHOD .. [pm]" font MONO size 13 color "#c9c6bf"
        text "OBSERVATION CONF .. [confidence]%" font MONO size 13 color "#c9c6bf"
        null height 14
        text "CANDIDATE POTENTIAL ..... NOT DETECTED" font MONO size 15 color "#912925"
        text "PLACEMENT ............... ROYCE TECHNOLOGIES" font MONO size 13 color "#c9c6bf"
        null height 14
        text "The instrument continues to measure capability. Results filed and held." font MONO size 12 color "#c9c6bf"
        text "[[ WITHHELD ]" font MONO size 12 color "#6e6a64"
        null height 14
        text "REVIEWED _______________" font MONO size 12 color "#6e6a64"
    hbox:
        xpos 60 yalign 0.95 spacing 20
        textbutton "SAVE A COPY" action Function(renpy.screenshot, "intake_result_file.png") text_font MONO text_size 13 text_color "#d4af37"
        textbutton "CLOSE" action Return() text_font MONO text_size 13 text_color "#d4af37"



