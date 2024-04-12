from typing import Callable, Dict, NamedTuple, Optional

from BaseClasses import Item, ItemClassification, MultiWorld


class RoomItem(Item):
    game = "Room"


class RoomItemData(NamedTuple):
    code: Optional[int] = None
    type: ItemClassification = ItemClassification.filler
    num_exist: int = 1
    can_create: Callable[[MultiWorld, int], bool] = lambda multiworld, player: True


item_data_table: Dict[str, RoomItemData] = {
    "A Small Key": RoomItemData(
        code=7430000,
        type=ItemClassification.progression
    ),
    "A Trophy": RoomItemData(
        code=7430001,
        type=ItemClassification.progression#,
        #can_create=lambda multiworld, player: bool(getattr(multiworld, "hard_mode")[player]),
    ),
    "A Tin of Mints": RoomItemData(
        code=7430002#,
        #can_create=lambda multiworld, player: False  # Only created from `get_filler_item_name`.
    ),
    #"The Urge to Push": CliqueItemData(
    #    type=ItemClassification.progression,
    #),
}

item_table = {name: data.code for name, data in item_data_table.items() if data.code is not None}
