from vehicle import Vehicle

class Garage:
    def __init__(self):
        self._vehicles: list[Vehicle] = []

    @property
    def vehicles(self) -> list[Vehicle]:
        return list(self._vehicles)

    def add_vehicle(self, vehicle: Vehicle) -> None:
        self._vehicles.append(vehicle)

    def remove_vehicle(self, vehicle: Vehicle) -> None:
        if vehicle in self._vehicles:
            self._vehicles.remove(vehicle)

    def sort_by_release_year(self) -> None:
        self._vehicles.sort()
    
    def empty_garage(self) -> None:
        self._vehicles.clear()

    def __str__(self) -> str:
        return "\n".join(str(vehicle) for vehicle in self._vehicles)