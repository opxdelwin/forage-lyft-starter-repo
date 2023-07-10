from datetime import date


class SpindlerBattery():
    def __init__(self, last_service_date: date, current_date: date):
        self.last_service_date = last_service_date
        self.current_date = current_date

        print("SpindlerBattery INIT")
        pass

    def needs_service(self):
        
        # if difference is more than 4, which is service tenure it returns true
        result =  self.current_date.year - self.last_service_date.year >= 2
        print("SpindlerBattery check returns:", result)
        return result