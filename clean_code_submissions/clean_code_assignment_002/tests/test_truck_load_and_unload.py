import pytest


def test_load_cargo_less_than_max_limit_when_truck_is_at_rest(truck):
    #arrange
    cargo_weight = 1
    #act
    truck.load(1)
    #assert
    assert truck.cargo_weight == cargo_weight

def test_load_cargo_more_than_max_limit_when_truck_is_at_rest(truck, capfd):
    #arrange
    #act
    truck.load(50)
    output = capfd.readouterr()
    #assert
    assert output.out == "Cannot load cargo more than max limit: 30\n"

def test_load_cargo_when_truck_is_at_motion(truck, capfd):
    truck.start_engine()
    truck.accelerate()
    truck.load(1)
    output = capfd.readouterr()
    assert output.out == "Cannot load cargo during motion\n"

def test_load_cargo_when_truck_is_started_and_at_rest(truck):
    truck.start_engine()
    truck.load(1)
    cargo_weight = 1
    assert truck.cargo_weight == cargo_weight

def test_load_cargo_when_truck_stopped_and_current_speed_equal_to_zero(truck):
    truck.start_engine()
    truck.stop_engine()
    truck.load(1)
    cargo_weight = 1
    assert truck.cargo_weight == cargo_weight

def test_load_cargo_when_stopped_current_speed_not_equal_to_zero(truck, capfd):
    truck.start_engine()
    truck.accelerate()
    truck.stop_engine()
    truck.load(1)
    output = capfd.readouterr()
    assert output.out == "Cannot load cargo during motion\n"

def test_load_invalid_cargo_weight(truck):
    with pytest.raises(Exception) as err:
        assert truck.load(-1)
    assert str(err.value) == "Invalid value for cargo_weight"

def test_unload_invalid_cargo_weight(truck):
    with pytest.raises(Exception) as err:
        assert truck.unload(-1)
    assert str(err.value) == "Invalid value for cargo_weight"

def test_unload_cargo_less_than_min_limit_when_truck_is_at_rest(truck, capfd):
    truck.unload(1)
    output = capfd.readouterr()
    assert output.out == "Cannot unload cargo less than min limit: 0\n"

def test_unloading_cargo_more_than_min_limit_when_truck_is_at_rest(truck):
    truck.load(20)
    truck.unload(1)
    cargo_weight = 19
    assert truck.cargo_weight == cargo_weight

def test_unloading_cargo_equal_to_zero_when_truck_is_at_rest(truck):
    with pytest.raises(Exception) as err:
        assert truck.unload(0)
    assert str(err.value) == "Invalid value for cargo_weight"

def test_unloading_cargo_when_truck_is_at_motion(truck, capfd):
    truck.load(10)
    truck.start_engine()
    truck.accelerate()
    truck.unload(1)
    output = capfd.readouterr()
    assert output.out == "Cannot unload cargo during motion\n"

def test_unload_cargo_when_truck_is_started_and_at_rest(truck):
    truck.start_engine()
    truck.load(10)
    truck.unload(1)
    cargo_weight = 9
    assert truck.cargo_weight == cargo_weight

def test_unload_cargo_when_truck_topped_and_current_speed_equal_to_zero(truck):
    truck.start_engine()
    truck.stop_engine()
    truck.load(10)
    truck.unload(1)
    cargo_weight = 9
    assert truck.cargo_weight == cargo_weight

def test_unload_cargo_stopped_current_speed_not_equal_to_zero(truck, capfd):
    truck.load(10)
    truck.start_engine()
    truck.accelerate()
    truck.stop_engine()
    truck.unload(1)
    output = capfd.readouterr()
    assert output.out == "Cannot unload cargo during motion\n"

def test_loading_cargo_equal_to_max_limit_when_truck_is_at_rest(truck):
    truck.load(30)
    cargo_weight = 30
    assert truck.cargo_weight == cargo_weight
