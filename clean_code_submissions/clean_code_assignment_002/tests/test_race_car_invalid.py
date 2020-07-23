import pytest

from race_car import RaceCar

@pytest.mark.parametrize("color, max_speed, acceleration, tyre_friction",
                         [("Red", -1, 10, 3), ("Red", 0, 10, 3)])
def test_invalid_max_speed_attr_for_race_car(color, max_speed,
                                             acceleration, tyre_friction):
    #arrange
    #act
    with pytest.raises(Exception) as err:
        assert RaceCar(color=color, max_speed=max_speed,
                       acceleration=acceleration, tyre_friction=tyre_friction)
    assert str(err.value) == "Invalid value for max_speed"
    #assert

@pytest.mark.parametrize("color, max_speed, acceleration, tyre_friction",
                         [("Red", 30, 0, 3), ("Red", 30, -1, 3)])
def test_invalid_acceleration_attr_for_race_car(color, max_speed,
                                                acceleration, tyre_friction):
    #arrange
    #act
    with pytest.raises(Exception) as err:
        assert RaceCar(color=color, max_speed=max_speed,
                       acceleration=acceleration, tyre_friction=tyre_friction)
    assert str(err.value) == "Invalid value for acceleration"
    #assert

@pytest.mark.parametrize("color, max_speed, acceleration, tyre_friction",
                         [("Red", 30, 10, 0), ("Red", 30, 10, -1)])
def test_invalid_tyre_friction_attr_for_race_car(color, max_speed,
                                                 acceleration, tyre_friction):
    #arrange
    #act
    with pytest.raises(Exception) as err:
        assert RaceCar(color=color, max_speed=max_speed,
                       acceleration=acceleration, tyre_friction=tyre_friction)
    assert str(err.value) == "Invalid value for tyre_friction"
    #assert
