from abc import ABC, abstractmethod

from auto_model import AutoModel
from manufacturer import Manufacturer


class Vehicle(ABC):
    """ Class for vehicles shows manufacturer, model, and fuel economy."""

    def __init__(
        self, manufacturer: Manufacturer, model: AutoModel, mpg: float
    ) -> None:
        self._manufacturer = manufacturer
        self._model = model
        self._mpg = mpg

    @property
    def manufacturer(self) -> Manufacturer:
        return self._manufacturer

    @property
    def model(self) -> AutoModel:
        return self._model

    @property
    def mpg(self) -> float:
        return self._mpg

    @property
    def release_year(self) -> int:
        return self._model.years[0]

    @abstractmethod
    def number_of_wheels(self) -> int:
        """Return the number of wheels on this vehicle."""

    def how_far_with(self, num_of_gallons: int) -> float:
        return self._mpg * num_of_gallons

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vehicle):
            return NotImplemented
        return self.release_year == other.release_year

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Vehicle):
            return NotImplemented
        return self.release_year < other.release_year
