import unittest

import pandas as pd
import plotly

from app.components import covid
from app.util.links import C19_DF


class TestCovid(unittest.TestCase):
    def test_init(self) -> None:
        output = covid.Model(C19_DF).data
        self.assertIsInstance(output, pd.DataFrame)

    def test_figure(self) -> None:
        output = covid.Model(C19_DF).Figure()
        self.assertIsInstance(
            output, plotly.graph_objs._figure.Figure,
        )

    def test_render(self) -> None:
        output = covid.Model(C19_DF).render()
        self.assertIsInstance(output, pd.DataFrame)


if __name__ in '__main__':
    unittest.main()
