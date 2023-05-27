"""Test module for stamina.py"""

import unittest

from meridiem.utilities.stamina import Stamina


class TestStamina(unittest.TestCase):
    def test_stamina_initialization(self):
        stamina = Stamina(30)
        self.assertEqual(stamina.stamina, 30)

        stamina = Stamina()
        self.assertEqual(stamina.stamina, 0)

    def test_get_rest_time(self):
        stamina = Stamina(0)
        self.assertAlmostEqual(stamina.get_rest_time(), 6 * 3 * 60 + 3 * 39 * 60)

        stamina = Stamina(Stamina.YELLOW_STAMINA)
        self.assertAlmostEqual(stamina.get_rest_time(), 6 * 3 * 60)

        stamina = Stamina(Stamina.MAX_STAMINA)
        self.assertAlmostEqual(stamina.get_rest_time(), 0.0)
