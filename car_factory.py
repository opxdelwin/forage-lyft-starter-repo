from components.engines.capulet_engine import CapuletEngine
from components.engines.sternman_engine import SternmanEngine
from components.engines.willoughby_engine import WilloughbyEngine

from components.batteries.spindler_battery import SpindlerBattery
from components.batteries.nubbin_battery import NubbinBattery

from components.tires.carrigan_tire import CarriganTire
from components.tires.octoprime_tire import OctoprimeTire

from datetime import datetime
from car import Car

class CarFactory:

    @staticmethod
    def create_calliope(last_service_mileage=10000, current_mileage=50000, last_service_date=datetime(2021, 2, 12), wear=[0.6,0.5,0.8,0.2]):

        print("Creating new Calliope")
        return Car(
            engine=CapuletEngine(last_service_mileage,current_mileage),
            battery=SpindlerBattery(last_service_date, current_date=datetime.now()),
            tire=CarriganTire(wear=wear)
        )


    @staticmethod
    def create_glissade(last_service_mileage=26000, current_mileage=50000, last_service_date=datetime(2022, 6, 19), wear = [0.9,0.8,0.2,0.6]):

        print("Creating new Glissade")
        return Car(
            engine=WilloughbyEngine(last_service_mileage,current_mileage),
            battery=SpindlerBattery(last_service_date, current_date=datetime.now()),
            tire=OctoprimeTire(wear=wear)
        )


    @staticmethod
    def create_palindrome(last_service_date=datetime(2022, 9, 23),warning_light_on=False, wear = [0.6, 0.6, 0.2, 0.8]):

        print("Creating new Palindrome")
        return Car(
            engine=SternmanEngine(warning_light_on),
            battery=SpindlerBattery(last_service_date, current_date=datetime.now()),
            tire=CarriganTire(wear=wear)
        )


    @staticmethod
    def create_rorschach(last_service_mileage = 50000, current_mileage = 59000, last_service_date = datetime(2023, 2, 11), wear = [0, 0.1, 0.3, 0.9]):

        print("Creating new Rorschach")
        return Car(
            engine=WilloughbyEngine(last_service_mileage, current_mileage),
            battery=NubbinBattery(last_service_date, current_date=datetime.now()),
            tire=OctoprimeTire(wear=wear)
        )


    @staticmethod
    def create_thovex(last_service_mileage = 19000, current_mileage = 50000, last_service_date = datetime(2022, 10, 11), wear = [0.8, 0.9, 0.7, 0]):

        print("Creating new Thovex")
        return Car(
            engine=CapuletEngine(last_service_mileage,current_mileage),
            battery=NubbinBattery(last_service_date, current_date=datetime.now()),
            tire=CarriganTire(wear=wear)
        )