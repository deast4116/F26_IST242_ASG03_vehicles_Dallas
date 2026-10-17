from manufacturer import Manufacturer
from automodel import Automodel

class Sedan(vehicle):
    def __init__(self, manufacturer:Manufacturer,
                 model: Automodel,
                 mpg: float,):
        super().__init__(manufacturer, model, mpg)

    def number_of_wheels(self) -> int:
        return 4

    def __str__(self):
        return f"{self.manufacturer} {self.model}, MPG: {self._mpg:.2f}"