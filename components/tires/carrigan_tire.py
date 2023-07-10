from components.tire import Tire

class CarriganTire(Tire):
    def __init__(self, wear : list) -> None:
        print("CarriganTire INIT")
        self.wear = wear
        super().__init__()


    def needs_servicing(self) -> bool:
        for i in self.wear:
            if i >= 0.9 : 
                return True
        return False