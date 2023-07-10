from components.tire import Tire

class OctoprimeTire(Tire):
    def __init__(self, wear : list) -> None:
        print("OctoprimeTire INIT")
        self.wear = wear
        super().__init__()
        pass

    def needs_servicing(self):
        sum = 0
        for i in self.wear:
            sum += i
            if sum >= 3:
                return True
        return False