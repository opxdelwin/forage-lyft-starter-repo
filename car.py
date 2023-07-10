from components.engine import Engine
from components.battery import Battery


class Car():
    def __init__(self, engine: Engine, battery: Battery):
        self.engine = engine
        self.battery = battery
        print("INIT CAR INSTANCE")


    def needs_service(self) -> bool:
        batteryResult = self.battery.needs_service()
        engineResult =  self.engine.needs_service()
        print("Overall service check result:", batteryResult or engineResult)
        return batteryResult or engineResult
    