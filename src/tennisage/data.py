import json
import re
from datetime import datetime

import pandas as pd
import requests

CAREER_URL = "https://www.tennisabstract.com/jsmatches/{}Career.js"
PROFILE_URL = "https://www.tennisabstract.com/jsmatches/{}.js"


def _clean_name(name):
    name = name.strip()
    if " " in name:
        name = "".join(word.capitalize() for word in name.split())
    return name


def _build_url(name):
    return CAREER_URL.format(_clean_name(name))


def _build_profile_url(name):
    return PROFILE_URL.format(_clean_name(name))


def _download_js(url):
    response = requests.get(url, timeout=30)
    if response.status_code != 200:
        raise ValueError("Player not found. Check the spelling of the name.")
    return response.text


def _extract_rows(js_text):
    found = re.search(r"morematchmx\s*=\s*(\[.*\])\s*;", js_text, re.DOTALL)
    if found is None:
        raise ValueError("No match data found for this player.")
    return json.loads(found.group(1))


def _to_date(text):
    return datetime.strptime(text, "%Y%m%d")


def _opponent_age(value, match_date):
    if value == "":
        return None
    if len(value) == 8 and value.isdigit():  # female files: birth date
        return (match_date - _to_date(value)).days / 365.25
    return float(value)  # male files: age already given


def _find_birth_date(profile_js):
    found = re.search(r"var\s+dob\s*=\s*(\d{8})", profile_js)
    if found is None:
        raise ValueError("Birth date not found for this player.")
    return _to_date(found.group(1))


def _clean_row(row, birth_date):
    match_date = _to_date(row[0])
    return {
        "date": match_date,
        "result": row[4],
        "opponent": row[11],
        "player_age": (match_date - birth_date).days / 365.25,
        "opponent_age": _opponent_age(row[16], match_date),
    }


def get_player_matches(name):
    career_js = _download_js(_build_url(name))
    profile_js = _download_js(_build_profile_url(name))
    rows = _extract_rows(career_js)
    birth_date = _find_birth_date(profile_js)
    df = pd.DataFrame([_clean_row(row, birth_date) for row in rows])
    df["age_diff"] = df["player_age"] - df["opponent_age"]
    return df
