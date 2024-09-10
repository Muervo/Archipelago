from typing import Callable

from BaseClasses import CollectionState, MultiWorld


#def get_button_rule(multiworld: MultiWorld, player: int) -> Callable[[CollectionState], bool]:
#    if getattr(multiworld, "hard_mode")[player]:
#        return lambda state: state.has("Button Activation", player)
#
#    return lambda state: True

def has_all_letters(state, player, characters, num_characters):
    for i in range(1, num_characters + 1):
        item_str = "Character " + str(i)
        if (not state.has(item_str, player)) and (item_str in characters):
            return False
    return True
