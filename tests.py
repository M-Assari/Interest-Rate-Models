
"""
Unit tests for Vasicek and Ho-Lee models.
"""
import unittest
import numpy as np
from models import VasicekModel, HoLeeModel

class TestInterestRateModels(unittest.TestCase):
    def test_vasicek_simulation(self):
        model = VasicekModel(0.1, 0.05, 0.02, 0.03)
        paths = model.simulate(T=1, dt=1/252, n_paths=5)
        self.assertEqual(paths.shape, (253, 5))

    def test_holee_simulation(self):
        model = HoLeeModel(0.001, 0.02, 0.03)
        paths = model.simulate(T=1, dt=1/252, n_paths=5)
        self.assertEqual(paths.shape, (253, 5))

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
