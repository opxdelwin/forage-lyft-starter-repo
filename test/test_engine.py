import unittest
from components.engines.capulet_engine import CapuletEngine
from components.engines.sternman_engine import SternmanEngine
from components.engines.willoughby_engine import WilloughbyEngine

class TestCapulet(unittest.TestCase):

    def test_engine_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0

        engine = CapuletEngine(last_service_mileage, current_mileage)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 30000
        last_service_mileage = 0

        engine = CapuletEngine(last_service_mileage, current_mileage)
        self.assertFalse(engine.needs_service())


class TestSternman(unittest.TestCase):

    def test_engine_should_be_serviced(self):
        warning_light_on = True

        engine = SternmanEngine(warning_light_on)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        warning_light_on = False

        engine = SternmanEngine(warning_light_on)
        self.assertFalse(engine.needs_service())


class TestWilloughby(unittest.TestCase):

    def test_engine_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0

        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 60000
        last_service_mileage = 0

        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertFalse(engine.needs_service())


if __name__ == '__main__':
    unittest.main()