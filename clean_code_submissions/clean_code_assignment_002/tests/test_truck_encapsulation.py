import pytest


def test_encapsulation_for_max_speed(truck):
    #arrange
    #act
    with pytest.raises(Exception) as err:
        truck.max_speed = 100
    #assert
    assert str(err.value) == "can't set attribute"

def test_encapsulation_for_acceleration(truck):
    #arrange
    #act
    with pytest.raises(Exception) as err:
        truck.acceleration = 100
    #assert
    assert str(err.value) == "can't set attribute"

def test_encapsulation_for_tyre_friction(truck):
    #arrange
    #act
    with pytest.raises(Exception) as err:
        truck.tyre_friction = 100
    #assert
    assert str(err.value) == "can't set attribute"

def test_encapsulation_for_color(truck):
    #arrange
    #act
    with pytest.raises(Exception) as err:
        truck.color = "brown"
    #assert
    assert str(err.value) == "can't set attribute"

def test_encapsulation_for_is_engine_started(truck):
    #arrange
    truck.start_engine()
    #act
    with pytest.raises(Exception) as err:
        truck.is_engine_started = False
    #assert
    assert str(err.value) == "can't set attribute"

def test_encapsulation_for_current_speed(truck):
    #arrange
    truck.start_engine()
    truck.accelerate()
    #act
    with pytest.raises(Exception) as err:
        truck.current_speed = 0
    #assert
    assert str(err.value) == "can't set attribute"
