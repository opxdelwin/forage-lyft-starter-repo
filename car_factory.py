from components.engines.capulet_engine import CapuletEngine
from components.engines.sternman_engine import SternmanEngine
from components.engines.willoughby_engine import WilloughbyEngine
from components.batteries.spindler_battery import SpindlerBattery
from components.batteries.nubbin_battery import NubbinBattery
from datetime import datetime
from car import Car

class CarFactory ():
    def create_calliope():
        print("Creating new Calliope")
        return Car(
            engine=CapuletEngine(last_service_mileage=10000,current_mileage=50000),
            battery=SpindlerBattery(last_service_date=datetime(2021, 2, 12), current_date=datetime.now()),
        )
    
    def create_glissade():
        print("Creating new Glissade")
        return Car(
            engine=WilloughbyEngine(last_service_mileage=26000,current_mileage=50000),
            battery=SpindlerBattery(last_service_date=datetime(2022, 6, 19), current_date=datetime.now()),
        )
    
    def create_palindrome():
        print("Creating new Palindrome")
        return Car(
            engine=SternmanEngine(warning_light_on=False),
            battery=SpindlerBattery(last_service_date=datetime(2022, 9, 23), current_date=datetime.now()),
        )
    
    def create_rorschach():
        print("Creating new Rorschach")
        return Car(
            engine=WilloughbyEngine(last_service_mileage=50000,current_mileage=59000),
            battery=NubbinBattery(last_service_date=datetime(2023, 2, 11), current_date=datetime.now()),
        )
    
    def create_thovex():
        print("Creating new Thovex")
        return Car(
            engine=CapuletEngine(last_service_mileage=19000,current_mileage=50000),
            battery=SpindlerBattery(last_service_date=datetime(2022, 10, 11), current_date=datetime.now()),
        )