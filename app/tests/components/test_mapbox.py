import unittest

import pandas as pd
import plotly

from app.components import mapbox
from app.config import MAPBOX_TOKEN
from app.util.links import CE_DF


class TestMapbox(unittest.TestCase):
    def test_init(self) -> None:
        output = mapbox.Model(CE_DF, MAPBOX_TOKEN)
        self.assertIsInstance(output.data, pd.DataFrame)
        self.assertIsInstance(output.token, str)

    def test_figure(self) -> None:
        output = mapbox.Model(CE_DF, MAPBOX_TOKEN).Figure()
        self.assertIsInstance(
            output, plotly.graph_objs._figure.Figure,
        )


if __name__ in '__main__':
    unittest.main()
