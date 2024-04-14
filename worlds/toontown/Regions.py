from typing import Dict, List, NamedTuple


class ToontownRegionData(NamedTuple):
    connecting_regions: List[str] = []


region_data_table: Dict[str, ToontownRegionData] = {
    "Menu": ToontownRegionData(["TTC"]),
    "TTC": ToontownRegionData(),
}
