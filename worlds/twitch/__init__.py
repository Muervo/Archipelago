from typing import List
from typing import Dict

from BaseClasses import Region, Tutorial
from worlds.AutoWorld import WebWorld, World
from .Items import TwitchItem, item_data_table, item_table
from .Locations import dice, TwitchLocation, TwitchLocationData, location_data_table, location_table, locked_locations
from .Options import TwitchOptions
from .Regions import region_data_table
#from .Rules import 


class TwitchWebWorld(WebWorld):
    theme = "partyTime"
    
    setup_en = Tutorial(
        tutorial_name="Start Guide",
        description="A guide to using the Twitch apworld.",
        language="English",
        file_name="guide_en.md",
        link="guide/en",
        authors=["LittleCube"]
    )
    
    tutorials = [setup_en]


class TwitchWorld(World):
    """ The apworld for your Twitch audience to participate in. """

    game = "Twitch"
    data_version = 1
    web = TwitchWebWorld()
    options_dataclass = TwitchOptions
    options: TwitchOptions
    location_name_to_id = location_table
    item_name_to_id = item_table

    def generate_early(self):
        options = self.fill_slot_data()
        for sides in dice:
            checks = options["d" + str(sides) + "_checks"]
            for i in range(checks + 1, sides + 1):
                check_str = "D" + str(sides) + ": Mystery Number " + str(i)
                del location_data_table[check_str]
                del location_table[check_str]
        for i in range(options["rps_checks"] + 1, 11):
            check_str = "RPS: Check " + str(i)
            del location_data_table[check_str]
            del location_table[check_str]
    
    def create_item(self, name: str) -> TwitchItem:
        return TwitchItem(name, item_data_table[name].type, item_data_table[name].code, self.player)

    def create_items(self) -> None:
        item_pool: List[TwitchItem] = []
        item_pool_count: Dict[str, int] = {}
        for name, item in item_data_table.items():
            if name not in item_pool_count:
                item_pool_count[name] = 0
            if item.code and item.can_create(self.multiworld, self.player):
                item_pool.append(self.create_item(name))
                item_pool_count[name] += 1

        self.multiworld.itempool += item_pool

    def create_regions(self) -> None:
        # Create regions.
        for region_name in region_data_table.keys():
            region = Region(region_name, self.player, self.multiworld)
            self.multiworld.regions.append(region)

        # Create locations.
        for region_name, region_data in region_data_table.items():
            region = self.multiworld.get_region(region_name, self.player)
            region.add_locations({
                location_name: location_data.address for location_name, location_data in location_data_table.items()
                if location_data.region == region_name and location_data.can_create(self.multiworld, self.player)
            }, TwitchLocation)
            region.add_exits(region_data_table[region_name].connecting_regions)

        # Place locked locations.
        for location_name, location_data in locked_locations.items():
            # Ignore locations we never created.
            if not location_data.can_create(self.multiworld, self.player):
                continue

            locked_item = self.create_item(location_data_table[location_name].locked_item)
            self.multiworld.get_location(location_name, self.player).place_locked_item(locked_item)

    def get_filler_item_name(self) -> str:
        return "out of pocket trug comment"

    def set_rules(self) -> None:
        options = self.fill_slot_data()
        for sides in dice:
            checks = options["d" + str(sides) + "_checks"]
            for i in range(1, checks + 1):
                self.multiworld.get_location("D" + str(sides) + ": Mystery Number " + str(i), self.player).access_rule = lambda state: state.has("D" + str(sides), self.player)

        for i in range(1, options["rps_checks"] + 1):
            self.multiworld.get_location("RPS: Check " + str(i), self.player).access_rule = lambda state: state.has("RPS", self.player)

        self.multiworld.get_location("Mystery Word", self.player).access_rule = lambda state: state.has("Letter 1", self.player) and state.has("Letter 2", self.player) and state.has("Letter 3", self.player) and state.has("Letter 4", self.player) and state.has("Letter 5", self.player)

        # Completion condition.
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)

    def fill_slot_data(self):
        return {
            "d6_checks": self.options.d6_checks.value,
            "d8_checks": self.options.d8_checks.value,
            "d10_checks": self.options.d10_checks.value,
            "d12_checks": self.options.d12_checks.value,
            "d15_checks": self.options.d15_checks.value,
            "rps_checks": self.options.rps_checks.value
        }
