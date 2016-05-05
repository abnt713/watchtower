from .tutorial import *
from .new_case import *
from .equipment import *
from .briefing import *
from .battle import *
from .ending import *

STATES = {
    "tutorial": TutorialState(),
    "new_case": NewCaseState(),
    "equipment": EquipmentState(),
    "briefing": BriefingState(),
    "battle": BattleState(),
    "ending": EndingState()
}


def get_state(state):
    global STATES
    return STATES[state]
