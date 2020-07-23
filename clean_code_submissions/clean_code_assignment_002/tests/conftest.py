import pytest


from car import Car
from race_car import RaceCar
from truck import Truck


@pytest.fixture
def car():
    car_obj = Car(color="Red", max_speed=30, acceleration=10, tyre_friction=3)
    return car_obj

@pytest.fixture
def car2():
    car_obj = Car(color="blue", max_speed=50, acceleration=20, tyre_friction=4)
    return car_obj

@pytest.fixture
def car3():
    car_obj = Car(color="blue", max_speed=30,
                  acceleration=3, tyre_friction=3)
    return car_obj

@pytest.fixture
def race_car():
    race_car_obj = RaceCar(color="Red", max_speed=30,
                           acceleration=10, tyre_friction=3)
    return race_car_obj

@pytest.fixture
def race_car2():
    race_car_obj = RaceCar(color="blue", max_speed=50,
                           acceleration=20, tyre_friction=4)
    return race_car_obj

@pytest.fixture
def race_car3():
    car_obj = RaceCar(color="blue", max_speed=10,
                      acceleration=3, tyre_friction=3)
    return car_obj

@pytest.fixture
def truck():  # Our Fixture function
    truck_obj = Truck(color="Red", max_speed=30,
                      acceleration=10, tyre_friction=3, max_cargo_weight=30)
    return truck_obj

@pytest.fixture
def truck2():  # Our Fixture function
    truck_obj = Truck(color="blue", max_speed=50, acceleration=20,
                      tyre_friction=4, max_cargo_weight=40)
    return truck_obj

@pytest.fixture
def truck3():  # Our Fixture function
    truck_obj = Truck(color="blue", max_speed=30, acceleration=3,
                      tyre_friction=3, max_cargo_weight=20)
    return truck_obj
