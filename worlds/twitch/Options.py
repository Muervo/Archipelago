from dataclasses import dataclass

from Options import PerGameCommonOptions, Range, FreeText, StartInventoryPool

from .Locations import MAX_RPS_CHECKS


class D6Checks(Range):
    """The number of checks shuffled for the D6 die."""
    display_name = "Number of D6 checks"
    range_start = 0
    range_end = 6
    default = 2


class D8Checks(Range):
    """The number of checks shuffled for the D8 die."""
    display_name = "Number of D8 checks"
    range_start = 0
    range_end = 8
    default = 2


class D10Checks(Range):
    """The number of checks shuffled for the D10 die."""
    display_name = "Number of D10 checks"
    range_start = 0
    range_end = 10
    default = 2


class D12Checks(Range):
    """The number of checks shuffled for the D12 die."""
    display_name = "Number of D12 checks"
    range_start = 0
    range_end = 12
    default = 2


class D15Checks(Range):
    """The number of checks shuffled for the D15 die."""
    display_name = "Number of D15 checks"
    range_start = 0
    range_end = 15
    default = 2


class RPSChecks(Range):
    """The number of checks shuffled for rock-paper-scissors."""
    display_name = "Number of rock-paper-scissors checks"
    range_start = 0
    range_end = MAX_RPS_CHECKS
    default = 2


class VictoryWord(FreeText):
    """The word to be guessed by the Audience to complete their goal."""
    display_name = "Victory Word"

@dataclass
class TwitchOptions(PerGameCommonOptions):
    d6_checks: D6Checks
    d8_checks: D8Checks
    d10_checks: D10Checks
    d12_checks: D12Checks
    d15_checks: D15Checks
    rps_checks: RPSChecks
    victory_word: VictoryWord
    start_inventory_from_pool: StartInventoryPool
