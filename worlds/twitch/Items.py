from typing import Callable, Dict, NamedTuple, Optional

from BaseClasses import Item, ItemClassification, MultiWorld


class TwitchItem(Item):
    game = "Twitch"


class TwitchItemData(NamedTuple):
    code: Optional[int] = None
    type: ItemClassification = ItemClassification.filler
    num_exist: int = 1
    can_create: Callable[[MultiWorld, int], bool] = lambda multiworld, player: True


item_data_table: Dict[str, TwitchItemData] = {
    "Progressive Luck": TwitchItemData(
        code=7339999,
        can_create=lambda multiworld, player: False
    ),
    "D6": TwitchItemData(
        code=7330000,
        type=ItemClassification.progression
    ),
    "D8": TwitchItemData(
        code=7330001,
        type=ItemClassification.progression
    ),
    "D10": TwitchItemData(
        code=7330002,
        type=ItemClassification.progression
    ),
    "D12": TwitchItemData(
        code=7330003,
        type=ItemClassification.progression
    ),
    "D15": TwitchItemData(
        code=7330004,
        type=ItemClassification.progression
    ),
    "D69": TwitchItemData(
        code=7330004,
        type=ItemClassification.progression
    ),
    "RPS": TwitchItemData(
        code=7330005,
        type=ItemClassification.progression
    ),
    "Victory": TwitchItemData(
        type=ItemClassification.progression
    )
}

MAX_LETTER_ITEMS = 128

for i in range(1, MAX_LETTER_ITEMS + 1):
    item_data_table["Character " + str(i)] = TwitchItemData(code=7330010 + i, type=ItemClassification.progression)

item_table = {name: data.code for name, data in item_data_table.items() if data.code is not None}
