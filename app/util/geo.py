import requests as req


def locate(city: str, state: str) -> list:
    """
    Fetch latitude & longitude of a given city & state
    by parsing a google maps web request.
    """
    url = f"https://www.google.com/maps/place/{city},+{state}/"
    resp = str(req.get(url).content)
    return parse_data(resp)


def parse_data(content: str) -> list:
    """
    Parse the web content to output
    a latitude & longitude.
    """
    target_start = content.find("https://www.google.com/maps/preview/place/")
    target_end = content[target_start:].find('"') + target_start
    target = (content[target_start:target_end]).split(',')

    lat = float(target[1][target[1].find("@") + 1:])
    lon = float(target[2])
    return [lat, lon]
