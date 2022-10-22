from dataclasses import dataclass
from datetime import datetime

from deploy_calender.month import Month, Zodiac


@dataclass
class Settings:
    month: Month
    sign: Zodiac


def _normalize_params(raw_params: dict[str, list[str]]) -> dict[str, str]:
    """
    Normalize param keys to lower and values to single string.

    If params has "duplication" we just select arbitrary version.
    """
    lower_keys = {k.lower(): v for k, v in raw_params.items()}
    return {k: v[0] for k, v in lower_keys.items()}


def get_settings(raw_params: dict[str, list[str]]) -> Settings:
    params = _normalize_params(raw_params)

    today = datetime.now()
    year = params.get("year", today.year)
    month = params.get("month", today.month)
    try:
        months = Month(int(year), int(month))
    except ValueError:
        months = Month(today.year, today.month)

    sign_text = params.get("sign", Zodiac.VIRGO.name)
    try:
        sign = Zodiac[sign_text.upper()]
    except KeyError:
        sign = Zodiac.VIRGO

    return Settings(months, sign)
