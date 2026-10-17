from auto_model import AutoModel
from manufacturer import Manufacturer
from vehicle import Vehicle


class Truck(Vehicle):
    def __init__(
        self,
        manufacturer: Manufacturer,
        model: AutoModel,
        mpg: float,
        is_dually: bool = False,
    ) -> None:
        super().__init__(manufacturer, model, mpg)
        self._is_dually = is_dually

    @property
    def is_dually(self) -> bool:
        return self._is_dually

    def number_of_wheels(self) -> int:
        return 6 if self._is_dually else 4

    def __str__(self) -> str:
        return (
            f"({self.manufacturer}) {self.model}, mpg: {self.mpg:.2f} "
            f"is dually truck: {self._is_dually}"
        )
