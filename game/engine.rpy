# Settings
define config.window_title = "Samsara Staffing Services - Intake Survey"
define config.screen_height = 600
define config.screen_width = 800
define config.rollback_enabled = False

define SANS = "DejaVuSans.ttf"
define MONO = "fonts/mono.ttf" if renpy.loadable("fonts/mono.ttf") else "DejaVu.ttf"

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
default q_total = 25
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
        store.qnum += 1
        store.confidence = min(97, store.confidence + 6)

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
        config.window_title = t

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
    padding(18, 9)
    xsize 400
style samsara_button_text is button_text:
    font SANS
    size 17
    color "#2b2b2b"
    hover_color "#000000"


