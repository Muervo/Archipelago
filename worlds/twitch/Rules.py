from typing import Callable

from BaseClasses import CollectionState, MultiWorld


#def get_button_rule(multiworld: MultiWorld, player: int) -> Callable[[CollectionState], bool]:
#    if getattr(multiworld, "hard_mode")[player]:
#        return lambda state: state.has("Button Activation", player)
#
#    return lambda state: True

def has_all_letters(state, player, num_letters):
    for i in range(1, num_letters + 1):
        if not state.has("Letter " + str(i), player):
            return False
    return True
