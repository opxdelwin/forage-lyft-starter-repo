from components.engine import Engine


class SternmanEngine(Engine):

    def __init__(self, warning_light_on : bool):
        print("SternmanEngine INIT")
        self.warning_light_on = warning_light_on
        super().__init__()
        pass


    def needs_service(self):
        # if difference is more than 4, which is service tenure it returns true
        print("SternmanEngine check returns:", self.warning_light_on)
        return self.warning_light_on
    
    #toggles current warning light value and returns new value.
    def toggle_warning_light(self):
        self.warning_light_on = not self.warning_light_on
        return self.warning_light_on