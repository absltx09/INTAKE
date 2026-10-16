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
        store.log.append({"q": store.q_label})



