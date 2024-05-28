from typing import Dict, List, NamedTuple


class TwitchRegionData(NamedTuple):
    connecting_regions: List[str] = []


region_data_table: Dict[str, TwitchRegionData] = {
    "Menu": TwitchRegionData(["The Chat"]),
    "The Chat": TwitchRegionData()
}
