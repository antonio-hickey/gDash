import unittest

from app.util import Nations, links


class TestUtils(unittest.TestCase):
    def test_convert_abbreviation(self) -> None:
        scenarios = ["USA", "CHN", "KOR", "BRA"]
        for scenario in scenarios:
            output = Nations.convert_abbreviation(scenario)
            if scenario == "USA":
                self.assertEqual(output, "United States")
            elif scenario == "CHN":
                self.assertEqual(output, "China")
            elif scenario == "KOR":
                self.assertEqual(output, "South Korea")
            elif scenario == "BRA":
                self.assertEqual(output, "Brazil")

    def test_links(self) -> None:
        self.assertEqual(
            links.OWID_COVID,
            "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv",
        )
        self.assertEqual(
            links.CFR_API,
            "https://microsites-live-backend.cfr.org/conflict/map/json",
        )
        self.assertEqual(
            links.GDACS,
            "https://www.gdacs.org/xml/rss_24h.xml",
        )
        self.assertEqual(
            links.C19_DF,
            "https://raw.githubusercontent.com/antonio-hickey/gDash/main/app/data/covid/world_c19.csv",
        )


if __name__ in '__main__':
    unittest.main()
