import pytest


def test_encapsulation_for_max_speed(car):
    #act
    with pytest.raises(Exception) as err:
        car.max_speed = 100
    #assert
    assert str(err.value) == "can't set attribute"

def test_encapsulation_for_acceleration(car):
    #act
    with pytest.raises(Exception) as err:
        car.acceleration = 100
    #assert
    assert str(err.value) == "can't set attribute"

def test_encapsulation_for_tyre_friction(car):
    #act
    with pytest.raises(Exception) as err:
        car.tyre_friction = 100
    #assert
    assert str(err.value) == "can't set attribute"

def test_encapsulation_for_color(car):
    #act
    with pytest.raises(Exception) as err:
        car.color = "brown"
    #assert
    assert str(err.value) == "can't set attribute"

def test_encapsulation_for_is_engine_started(car):
    #arrange
    car.start_engine()
    #act
    with pytest.raises(Exception) as err:
        car.is_engine_started = False
    #assert
    assert str(err.value) == "can't set attribute"

def test_encapsulation_for_current_speed(car):
    #arrange
    car.start_engine()
    car.accelerate()
    #act
    with pytest.raises(Exception) as err:
        car.current_speed = 0
    #assert
    assert str(err.value) == "can't set attribute"
