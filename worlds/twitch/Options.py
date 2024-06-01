from dataclasses import dataclass

from Options import PerGameCommonOptions, Range

from .Locations import MAX_RPS_CHECKS


#class HardMode(Toggle):
#    """Only for the most masochistically inclined... Requires button activation!"""
#    display_name = "Hard Mode"


#class ButtonColor(Choice):
#    """Customize your button! Now available in 12 unique colors."""
#    display_name = "Button Color"
#    option_red = 0
#    option_orange = 1
#    option_yellow = 2
#    option_green = 3
#    option_cyan = 4
#    option_blue = 5
#    option_magenta = 6
#    option_purple = 7
#    option_pink = 8
#    option_brown = 9
#    option_white = 10
#    option_black = 11


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


@dataclass
class TwitchOptions(PerGameCommonOptions):
    d6_checks: D6Checks
    d8_checks: D8Checks
    d10_checks: D10Checks
    d12_checks: D12Checks
    d15_checks: D15Checks
    rps_checks: RPSChecks
