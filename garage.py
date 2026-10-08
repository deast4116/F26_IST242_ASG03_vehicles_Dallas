from vehicle import Vehicle

class Garage:
    def __init__(self):
        self.vehicles = []

    @property
    def vehicles(self) -> list[Vehicle]:
        return list(self._vehicles)

    def add_vehicle(self, vehicle: Vehicle):
        self.vehicles.append(vehicle)

    def remove_vehicle(self, vehicle: Vehicle):
        if vehicle in self.vehicles:
            self.vehicles.remove(vehicle)

    def sort_by_release_year(self):
        self.vehicles.sort(key=lambda v: v.model.years[0] if v.model.years else float('inf'))
    
    def empty_garage(self) -> None:
        self.vehicles.clear()

    