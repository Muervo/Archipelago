from typing import Callable, Dict, NamedTuple, Optional

from BaseClasses import Item, ItemClassification, MultiWorld


class ToontownItem(Item):
    game = "Toontown"


class ToontownItemData(NamedTuple):
    code: Optional[int] = None
    type: ItemClassification = ItemClassification.filler
    num_exist: int = 1
    can_create: Callable[[MultiWorld, int], bool] = lambda multiworld, player: True


item_data_table: Dict[str, ToontownItemData] = {
    "A Message": ToontownItemData(
        code=3470000,
        type=ItemClassification.progression
    ),
    "10 Jellybeans": ToontownItemData(
        code=3470001,
        type=ItemClassification.filler
    )
}

item_table = {name: data.code for name, data in item_data_table.items() if data.code is not None}
