"""
The main entry point for assignment 03 vehicle Hierarchy with ABC

Author: Dallas East
"""

from auto_model import AutoModel
from garage import Garage
from manufacturer import Manufacturer
from sedan import Sedan
from truck import Truck


def main() -> None:
    ford = Manufacturer("Ford", "USA")
    honda = Manufacturer("Honda", "Japan")
    bmw = Manufacturer("BMW", "Germany")
    toyota = Manufacturer("Toyota", "Japan")

    f150 = Truck(ford, AutoModel("F150", True, [2020, 2021, 2022]), 20.0)
    civic = Sedan(honda, AutoModel("Civic", False, [1996, 1997, 1998]), 28.0)
    m3 = Sedan(
        bmw,
        AutoModel("M3 Limited", False, [2015, 2016, 2017, 2018]),
        30.0,
    )
    tundra = Truck(
        toyota, AutoModel("Tundra", False, [1987, 1988]), 30.0, is_dually=True
    )

    g = Garage()
    for vehicle in (f150, civic, m3, tundra):
        g.add_vehicle(vehicle)

    print("Before sorting:")
    print(g)
    g.sort_by_release_year()
    print("\nAfter sorting:")
    print(g)


if __name__ == "__main__":
    main()