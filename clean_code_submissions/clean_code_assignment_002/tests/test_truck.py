def test_start_engine(truck):
    #arrange
    is_engine_started = True
    #act
    truck.start_engine()
    #assert
    assert truck.is_engine_started == is_engine_started

def test_start_engine_when_truck_engine_is_started_twice(truck):
    #arrange
    truck.start_engine()
    is_engine_started = True
    #act
    truck.start_engine()
    #assert
    assert truck.is_engine_started == is_engine_started

def test_current_speed_to_zero_for_newly_created_truck(truck):
    #arrange
    current_speed = 0
    #act
    #arrange
    assert truck.current_speed == current_speed

def test_current_speed_to_zero_even_after_engine_start(truck):
    #arrange
    current_speed = 0
    #act
    truck.start_engine()
    #assert
    assert truck.current_speed == current_speed

def test_accelerate_truck_when_engine_is_not_started(truck):
    #arrange
    current_speed = 0
    #act
    truck.accelerate()
    #assert
    assert truck.current_speed == current_speed

def test_accelerate_with_different_acceleration_when_engine_not_started(truck):
    #arrange
    truck.accelerate()
    current_speed = 0
    #act
    truck.accelerate()
    #assert
    assert truck.current_speed == current_speed

def test_accelerate_truck(truck):
    #arrange
    truck.start_engine()
    current_speed = 10
    #act
    truck.accelerate()
    #assert
    assert truck.current_speed == current_speed

def test_accelerate_truck_with_different_acceleration(truck):
    #arrange
    truck.start_engine()
    truck.accelerate()
    current_speed = 20
    #act
    truck.accelerate()
    #assert
    assert truck.current_speed == current_speed

def test_accelerate_truck_with_current_speed_more_than_max_limit(truck):
    #arrange
    truck.start_engine()
    truck.accelerate()
    truck.accelerate()
    truck.accelerate()
    current_speed = 30
    #act
    truck.accelerate()
    #assert
    assert truck.current_speed == current_speed

def test_accelerate_with_different_acceleration_more_than_max_limit(truck):
    #arrange
    truck.start_engine()
    truck.accelerate()
    truck.accelerate()
    truck.accelerate()
    current_speed = 30
    #act
    truck.accelerate()
    #assert
    assert truck.current_speed == current_speed

def test_apply_brake_when_truck_is_at_rest(truck):
    #arrange
    current_speed = 0
    #act
    truck.apply_brakes()
    #assert
    assert truck.current_speed == current_speed

def test_apply_brake_when_truck_current_speed_more_than_tyre_friction(truck):
    #arrange
    truck.start_engine()
    truck.accelerate()
    current_speed = 7
    #act
    truck.apply_brakes()
    #assert
    assert truck.current_speed == current_speed

def test_apply_break_diff_acceleration_speed_more_than_tyre_friction(truck):
    #arrange
    truck.start_engine()
    truck.accelerate()
    truck.accelerate()
    current_speed = 17
    #act
    truck.apply_brakes()
    #assert
    assert truck.current_speed == current_speed

def test_apply_brake_when_current_speed_is_less_than_tyrefriction(truck):
    #arrange
    truck.start_engine()
    truck.accelerate()
    truck.apply_brakes()
    truck.apply_brakes()
    truck.apply_brakes()
    truck.apply_brakes()
    current_speed = 0
    #act
    truck.apply_brakes()
    #assert
    assert truck.current_speed == current_speed

def test_sound_horn_when_truck_engine_not_started(truck, capfd):
    #arrange
    #act
    truck.sound_horn()
    output = capfd.readouterr()
    #assert
    assert output.out == "Start the engine to sound_horn\n"

def test_sound_horn_when_truck_is_started(truck, capfd):
    #arrange
    truck.start_engine()
    #act
    truck.sound_horn()
    output = capfd.readouterr()
    #assert
    assert output.out == "Honk Honk\n"

def test_stop_engine_when_engine_is_started(truck):
    #arrange
    truck.start_engine()
    is_engine_started = False
    #act
    truck.stop_engine()
    #assert
    assert truck.is_engine_started == is_engine_started

def test_stop_engine_when_engine_is_already_stopped(truck):
    #arrange
    truck.stop_engine()
    is_engine_started = False
    #act
    truck.stop_engine()
    #assert
    assert truck.is_engine_started == is_engine_started

def test_stop_engine_when_engine_is_in_running(truck):
    #arrange
    truck.start_engine()
    truck.accelerate()
    is_engine_started = False
    #act
    truck.stop_engine()
    #assert
    assert truck.is_engine_started == is_engine_started
