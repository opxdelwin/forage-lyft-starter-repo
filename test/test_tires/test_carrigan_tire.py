import unittest
from components.tires.carrigan_tire import CarriganTire

class TestCarrigan(unittest.TestCase):

    # test returns true if any one wear is >= 0.9

    def test_tire_needs_service(self):
        tire = CarriganTire([0.1, 0.2, 0.91, 0.8])
        self.assertTrue(tire.needs_servicing())

    def test_tire_does_not_need_service(self):
        tire = CarriganTire([0.1, 0.2, 0.8, 0.8])
        self.assertFalse(tire.needs_servicing())

if __name__ == '__main__':
    unittest.main()