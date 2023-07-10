import unittest

from components.tires.octoprime_tire import OctoprimeTire

class TestOctoprime(unittest.TestCase):

    # test returns true when sum of individual wear is >= 3

    def test_tire_need_servicing(self):
        wear = [1,1,1,0]
        tire = OctoprimeTire(wear=wear)
        self.assertTrue(tire.needs_servicing())

    def test_tire_does_not_need_servicing(self):
        wear = [1,1,0.8,0]
        tire = OctoprimeTire(wear=wear)
        self.assertFalse(tire.needs_servicing())


if __name__ == '__main__':
    unittest.main()