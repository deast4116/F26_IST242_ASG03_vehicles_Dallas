from auto_model import AutoModel
from manufacturer import Manufacturer
from vehicle import Vehicle


class Sedan(Vehicle):
    def __init__(
        self, manufacturer: Manufacturer, model: AutoModel, mpg: float
    ) -> None:
        super().__init__(manufacturer, model, mpg)

    def number_of_wheels(self) -> int:
        return 4

    def __str__(self) -> str:
        return f"({self.manufacturer}) {self.model}, mpg: {self.mpg:.2f}"
