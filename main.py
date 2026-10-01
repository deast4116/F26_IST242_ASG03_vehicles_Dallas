"""
The main entry point for assignment 03 vehicle Hierarchy with ABC

Author: Dallas East

"""
from manufacturer import Manufacturer

def main():

    ford = Manufacturer("Ford", "USA")
    honda = Manufacturer("Honda", "Japan")
    bmw = Manufacturer("BMW", "Germany")
    toyota = Manufacturer("Toyota", "Japan")

    year_list = [2020, 2021]
    model1 = AutoModel("F150", True, year_list)

    year_list.append(2022)
    print(model1)

    

if __name__ == main:
    main()