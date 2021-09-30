import unittest

import pandas as pd
import plotly

from app.components import economics
from app.util.links import GDP_DF


class TestEconomics(unittest.TestCase):
    def test_init(self) -> None:
        output = economics.Model(GDP_DF).data
        self.assertIsInstance(
            output, pd.DataFrame,
        )

    def test_figure(self) -> None:
        output = economics.Model(GDP_DF).Figure()
        self.assertIsInstance(
            output, plotly.graph_objs._figure.Figure,
        )


if __name__ in '__main__':
    unittest.main()
