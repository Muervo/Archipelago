from typing import Dict, List, NamedTuple


class RoomRegionData(NamedTuple):
    connecting_regions: List[str] = []


region_data_table: Dict[str, RoomRegionData] = {
    "Menu": RoomRegionData(["The Room"]),
    "The Room": RoomRegionData(),
}
