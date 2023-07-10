from components.engine import Engine
from components.battery import Battery
from components.tire import Tire


class Car():
    def __init__(self, engine: Engine, battery: Battery, tire: Tire):
        self.engine = engine
        self.battery = battery
        self.tire = tire
        print("INIT CAR INSTANCE")


    def needs_service(self) -> bool:
        batteryResult = self.battery.needs_service()
        engineResult =  self.engine.needs_service()
        tireResult = self.tire.needs_service()
        print("Overall service check result:", batteryResult or engineResult or tireResult)
        return batteryResult or engineResult or tireResult