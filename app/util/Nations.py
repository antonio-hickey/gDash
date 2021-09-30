from app.data.util.nations import hashmap


def convert_abbreviation(abbrev: str) -> str:
    return hashmap[abbrev]
