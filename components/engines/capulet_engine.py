from components.engine import Engine


class CapuletEngine(Engine):
   def __init__(self, last_service_mileage : int, current_mileage:int):
      self.last_service_mileage = last_service_mileage
      self.current_mileage = current_mileage
      
      print("CapuletEngine INIT")
      super().__init__()
      pass


   def needs_service(self):
      # if difference is more than 4, which is service tenure it returns true
        result =  self.current_mileage - self.last_service_mileage >  30000
        print("CapuletEngine check returns:", result)
        return result