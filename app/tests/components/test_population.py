import unittest

import pandas as pd
import plotly

from app.components import population
from app.util.links import POP_DF


class TestPopulation(unittest.TestCase):
    def test_init(self) -> None:
        output = population.Model(POP_DF).data
        self.assertIsInstance(output, pd.DataFrame)

    def test_figure(self) -> None:
        output = population.Model(POP_DF).Figure()
        self.assertIsInstance(
            output, plotly.graph_objs._figure.Figure,
        )


if __name__ in '__main__':
    unittest.main()
