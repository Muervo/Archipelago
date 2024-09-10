from typing import List
from typing import Dict

from BaseClasses import Region, Tutorial, ItemClassification
from worlds.AutoWorld import WebWorld, World
from .Items import TwitchItem, MAX_LETTER_ITEMS, item_data_table, item_table
from .Locations import dice, MAX_RPS_CHECKS, TwitchLocation, TwitchLocationData, location_data_table, location_table, locked_locations
from .Options import TwitchOptions
from .Regions import region_data_table
from .Rules import has_all_letters


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
    location_data_table_copy = {}
    item_data_table_copy = {}
    num_locations = 0
    num_items = 0
    luck_count = 0
    spaces_count = 0

    def generate_early(self):
        self.location_data_table_copy = location_data_table.copy()
        options = self.fill_slot_data()
        victory_word = options["victory_word"]
        if len(victory_word) > MAX_LETTER_ITEMS:
            raise Exception(f"Your word/phrase must be {MAX_LETTER_ITEMS} characters or less! ({victory_word})")
        for sides in dice:
            checks = options["d" + str(sides) + "_checks"]
            for i in range(checks + 1, sides + 1):
                check_str = "D" + str(sides) + ": Mystery Number " + str(i)
                del self.location_data_table_copy[check_str]
        for i in range(options["rps_checks"] + 1, MAX_RPS_CHECKS + 1):
            check_str = "RPS: Check " + str(i)
            del self.location_data_table_copy[check_str]

        self.item_data_table_copy = item_data_table.copy()
        if self.options.give_spaces.value:
            for i in range(1, len(self.options.victory_word.value) + 1):
                if self.options.victory_word.value[i - 1] == " ":
                    self.spaces_count += 1
                    item_str = "Character " + str(i)
                    del self.item_data_table_copy[item_str]
        for i in range(len(self.options.victory_word.value) + 1, MAX_LETTER_ITEMS + 1):
            item_str = "Character " + str(i)
            del self.item_data_table_copy[item_str]

    def create_item(self, name: str) -> TwitchItem:
        return TwitchItem(name, self.item_data_table_copy[name].type, self.item_data_table_copy[name].code, self.player)

    def create_items(self) -> None:
        item_pool: List[TwitchItem] = []
        item_pool_count: Dict[str, int] = {}
        for name, item in self.item_data_table_copy.items():
            if name not in item_pool_count:
                item_pool_count[name] = 0
            if item.code and item.can_create(self.multiworld, self.player):
                for i in range(0, item.num_exist):
                    item_pool.append(self.create_item(name))
                    item_pool_count[name] += 1
                    self.num_items += 1
        if self.num_items < self.num_locations:
            filler_item_name = self.get_filler_item_name()
            for i in range(0, self.num_locations - self.num_items):
                item_pool.append(self.create_item(filler_item_name))
                item_pool_count[filler_item_name] += 1
                self.luck_count += 1
        self.num_items += self.luck_count

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
                location_name: location_data.address for location_name, location_data in self.location_data_table_copy.items()
                if location_data.region == region_name and location_data.can_create(self.multiworld, self.player)
            }, TwitchLocation)
            region.add_exits(region_data_table[region_name].connecting_regions)
            self.num_locations += len(region.locations)
        # Place locked locations.
        for location_name, location_data in locked_locations.items():
            # Ignore locations we never created.
            if not location_data.can_create(self.multiworld, self.player):
                continue

            locked_item = self.create_item(self.location_data_table_copy[location_name].locked_item)
            self.multiworld.get_location(location_name, self.player).place_locked_item(locked_item)
            self.num_locations -= 1

    def get_filler_item_name(self) -> str:
        return "Progressive Luck"

    def set_rules(self) -> None:
        options = self.fill_slot_data()
        max_sides = dice[len(dice) - 1]
        for sides in dice:
            checks = options["d" + str(sides) + "_checks"]
            if sides == dice[0]:
                for i in range(1, checks + 1):
                    checks = options["d" + str(sides) + "_checks"]
                    self.multiworld.get_location("D" + str(sides) + ": Mystery Number " + str(i), self.player).access_rule = lambda state: state.has("D" + str(sides), self.player)
                continue
            for i in range(1, checks + 1):
                self.multiworld.get_location("D" + str(sides) + ": Mystery Number " + str(i), self.player).access_rule = lambda state: state.has("D" + str(sides), self.player)

        for i in range(1, options["rps_checks"] + 1):
            self.multiworld.get_location("RPS: Check " + str(i), self.player).access_rule = lambda state: state.has("RPS", self.player)

        self.multiworld.get_location("Victory Word", self.player).access_rule = lambda state: has_all_letters(state, self.player, self.item_data_table_copy, len(self.options.victory_word.value))

        # Completion condition.
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)

    def fill_slot_data(self):
        return {
            "d6_checks": self.options.d6_checks.value,
            "d8_checks": self.options.d8_checks.value,
            "d10_checks": self.options.d10_checks.value,
            "d12_checks": self.options.d12_checks.value,
            "d15_checks": self.options.d15_checks.value,
            "d69_checks": self.options.d69_checks.value,
            "rps_checks": self.options.rps_checks.value,
            "give_spaces": self.options.give_spaces.value,
            "victory_word": self.options.victory_word.value,
            "victory_word_size": len(self.options.victory_word.value),
            "luck_count": self.luck_count
        }
