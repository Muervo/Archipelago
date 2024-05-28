from typing import Callable, Dict, NamedTuple, Optional

from BaseClasses import Location, MultiWorld


class TwitchLocation(Location):
    game = "Twitch"


class TwitchLocationData(NamedTuple):
    region: str = "The Chat"
    address: Optional[int] = None
    can_create: Callable[[MultiWorld, int], bool] = lambda multiworld, player: True
    locked_item: Optional[str] = None


location_data_table: Dict[str, TwitchLocationData] = {
    "First Chat": TwitchLocationData(
        address=7330000
    ),
    #"D6: Mystery Number 1": TwitchLocationData(
    #    address=7330001
    #),
    #"D6: Mystery Number 2": TwitchLocationData(
    #    address=7330002
    #),
    #"D8: Mystery Number 1": TwitchLocationData(
    #    address=7330011
    #),
    #"D8: Mystery Number 2": TwitchLocationData(
    #    address=7330012
    #),
    #"D10: Mystery Number 1": TwitchLocationData(
    #    address=7330021
    #),
    #"D10: Mystery Number 2": TwitchLocationData(
    #    address=7330022
    #),
    #"D12: Mystery Number 1": TwitchLocationData(
    #    address=7330031
    #),
    #"D12: Mystery Number 2": TwitchLocationData(
    #    address=7330032
    #),
    #"D15: Mystery Number 1": TwitchLocationData(
    #    address=7330041
    #),
    #"D15: Mystery Number 2": TwitchLocationData(
    #    address=7330042
    #),
    "Mystery Word": TwitchLocationData(
        locked_item="Victory"
    )
}

dice = [6, 8, 10, 12, 15]

for sides in dice:
    for i in range(1, sides + 1):
        print("address: " + str(7330000 + sides*100 + i))
        location_data_table["D" + str(sides) + ": Mystery Number " + str(i)] = TwitchLocationData(address=7330000 + sides*100 + i)

for i in range(1, 11):
    location_data_table["RPS: Check " + str(i)] = TwitchLocationData(address=7337300 + i)

location_table = {name: data.address for name, data in location_data_table.items() if data.address is not None}
locked_locations = {name: data for name, data in location_data_table.items() if data.locked_item}
