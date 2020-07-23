import pytest


from truck import Truck


@pytest.mark.parametrize("color, max_speed, acceleration, tyre_friction, max_cargo_weight",
                         [("Red", -1, 10, 3, 10), ("Red", 0, 10, 3, 10)])
def test_invalid_max_speed_attr_for_truck(color, max_speed, acceleration,
                                          tyre_friction, max_cargo_weight):
    #arrange
    #act
    with pytest.raises(Exception) as err:
        assert Truck(color=color, max_speed=max_speed,
                     acceleration=acceleration, tyre_friction=tyre_friction,
                     max_cargo_weight=max_cargo_weight)
    #assert
    assert str(err.value) == "Invalid value for max_speed"

@pytest.mark.parametrize("color, max_speed, acceleration, tyre_friction, max_cargo_weight",
                         [("Red", 30, -1, 3, 10), ("Red", 30, 0, 3, 10)])
def test_invalid_acceleration_attr_for_truck(color, max_speed, acceleration,
                                             tyre_friction, max_cargo_weight):
    #arrange
    #act
    with pytest.raises(Exception) as err:
        assert Truck(color=color, max_speed=max_speed,
                     acceleration=acceleration,
                     tyre_friction=tyre_friction,
                     max_cargo_weight=max_cargo_weight)
    #assert
    assert str(err.value) == "Invalid value for acceleration"

@pytest.mark.parametrize("color, max_speed, acceleration, tyre_friction, max_cargo_weight",
                         [("Red", 30, 10, -1, 10), ("Red", 30, 10, 0, 10)])
def test_invalid_tyre_friction_attr_for_truck(color, max_speed, acceleration,
                                              tyre_friction, max_cargo_weight):
    #arrange
    #act
    with pytest.raises(Exception) as err:
        assert Truck(color=color, max_speed=max_speed,
                     acceleration=acceleration, tyre_friction=tyre_friction,
                     max_cargo_weight=max_cargo_weight)
    #assert
    assert str(err.value) == "Invalid value for tyre_friction"

@pytest.mark.parametrize("color, max_speed, acceleration, tyre_friction, max_cargo_weight",
                         [("Red", 30, 10, 3, -1), ("Red", 30, 10, 3, 0)])
def test_invalid_max_cargo_weight_attr(color, max_speed, acceleration,
                                       tyre_friction, max_cargo_weight):
    #arrange
    #act
    with pytest.raises(Exception) as err:
        assert Truck(color=color, max_speed=max_speed,
                     acceleration=acceleration,
                     tyre_friction=tyre_friction,
                     max_cargo_weight=max_cargo_weight)
    #assert
    assert str(err.value) == "Invalid value for max_cargo_weight"
