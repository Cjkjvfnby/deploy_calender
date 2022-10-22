from dataclasses import dataclass
from enum import Enum

# typing helpers
Weekday = int
Day = int


@dataclass
class Month:
    year: int
    month: int


class Zodiac(Enum):
    ARIES = "♈"
    TAURUS = "♉"
    GEMINI = "♊"
    CANCER = "♋"
    LEO = "♌"
    VIRGO = "♍"
    LIBRA = "♎"
    SCORPIO = "♏"
    SAGITTARIUS = "♐"
    CAPRICORN = "♑"
    AQUARIUS = "♒"
    PISCES = "♓"
