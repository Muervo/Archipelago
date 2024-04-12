from typing import Callable, Dict, NamedTuple, Optional

from BaseClasses import Location, MultiWorld


class RoomLocation(Location):
    game = "Clique"


class RoomLocationData(NamedTuple):
    region: str
    address: Optional[int] = None
    can_create: Callable[[MultiWorld, int], bool] = lambda multiworld, player: True
    locked_item: Optional[str] = None


location_data_table: Dict[str, RoomLocationData] = {
    "Cabinet": RoomLocationData(
        region="The Room",
        address=7430000#,
        #locked_item = "Small Key"
    ),
    #"The Item on the Desk": CliqueLocationData(
    #    region="The Button Realm",
    #    address=69696968,
    #    can_create=lambda multiworld, player: bool(getattr(multiworld, "hard_mode")[player]),
    #),
    "Small Table - 1": RoomLocationData(
        region="The Room",
        address=7430001
    ),
    "Small Table - 2": RoomLocationData(
        region="The Room",
        address=7430002
    ),
}

location_table = {name: data.address for name, data in location_data_table.items() if data.address is not None}
locked_locations = {name: data for name, data in location_data_table.items() if data.locked_item}
