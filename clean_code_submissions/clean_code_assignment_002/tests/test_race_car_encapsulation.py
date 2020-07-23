import pytest


def test_encapsulation_for_max_speed(race_car):
    #act
    with pytest.raises(Exception) as err:
        race_car.max_speed = 100
    #assert
    assert str(err.value) == "can't set attribute"

def test_encapsulation_for_acceleration(race_car):
    #act
    with pytest.raises(Exception) as err:
        race_car.acceleration = 100
    #assert
    assert str(err.value) == "can't set attribute"

def test_encapsulation_for_tyre_friction(race_car):
    #act
    with pytest.raises(Exception) as err:
        race_car.tyre_friction = 100
    #assert
    assert str(err.value) == "can't set attribute"

def test_encapsulation_for_color(race_car):
    #act
    with pytest.raises(Exception) as err:
        race_car.color = "brown"
    #assert
    assert str(err.value) == "can't set attribute"

def test_encapsulation_for_is_engine_started(race_car):
    #arrange
    race_car.start_engine()
    #act
    with pytest.raises(Exception) as err:
        race_car.is_engine_started = False
    #assert
    assert str(err.value) == "can't set attribute"

def test_encapsulation_for_current_speed(race_car):
    #arrange
    race_car.start_engine()
    race_car.accelerate()
    #act
    with pytest.raises(Exception) as err:
        race_car.current_speed = 0
    #assert
    assert str(err.value) == "can't set attribute"
