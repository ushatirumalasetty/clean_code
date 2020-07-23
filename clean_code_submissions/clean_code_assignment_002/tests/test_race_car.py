def test_start_engine(race_car):
    race_car.start_engine()
    is_engine_started = True
    assert race_car.is_engine_started == is_engine_started

def test_start_engine_when_engine_is_started_twice(race_car):
    race_car.start_engine()
    race_car.start_engine()
    is_engine_started = True
    assert race_car.is_engine_started == is_engine_started

def test_start_engine_when_multiple_objects_are_present(race_car, race_car2):
    race_car.start_engine()
    is_engine_started = False
    assert race_car2.is_engine_started == is_engine_started


def test_current_speed_before_engine_is_started(race_car):
    current_speed = 0
    assert race_car.current_speed == current_speed


def test_current_speed_after_engine_is_started(race_car):
    race_car.start_engine()
    current_speed = 0
    assert race_car.current_speed == current_speed

def test_accelerate_when_engine_is_not_started(race_car):
    race_car.accelerate()
    current_speed = 0
    assert race_car.current_speed == current_speed

def test_accelerate_with_different_acceleration_when_engine_is_not_started(race_car):
    race_car.accelerate()
    race_car.accelerate()
    current_speed = 0
    assert race_car.current_speed == current_speed

def test_accelerate_when_nitro_is_not_available(race_car):
    race_car.start_engine()
    race_car.accelerate()
    race_car.accelerate()
    current_speed = 20
    assert race_car.current_speed == current_speed

def test_accelerate_when_nitro_is_available_within_max_speed(race_car):
    race_car.start_engine()
    race_car.accelerate()
    race_car.accelerate()
    race_car.apply_brakes()
    race_car.accelerate()
    current_speed = 30
    assert race_car.current_speed == current_speed

def test_accelerate_when_nitro_is_available_exceed_max_speed(race_car):
    race_car.start_engine()
    race_car.accelerate()
    race_car.accelerate()
    race_car.apply_brakes()
    race_car.accelerate()
    race_car.accelerate()
    current_speed = 30
    assert race_car.current_speed == current_speed


def test_accelerate_with_different_acceleration(race_car):
    race_car.start_engine()
    race_car.accelerate()
    race_car.accelerate()
    current_speed = 20
    assert race_car.current_speed == current_speed


def test_accelerate_when_current_speed_exceed_max_speed(race_car):
    race_car.start_engine()
    race_car.accelerate()
    race_car.accelerate()
    race_car.accelerate()
    race_car.accelerate()
    current_speed = 30
    assert race_car.current_speed == current_speed

def test_accelerate_when_current_speed_equal_to_max_speed(race_car):
    race_car.start_engine()
    race_car.accelerate()
    race_car.accelerate()
    race_car.accelerate()
    current_speed = 30
    assert race_car.current_speed == current_speed

def test_accelerate_with_different_acceleration_more_than_max_limit(race_car):
    race_car.start_engine()
    race_car.accelerate()
    race_car.accelerate()
    race_car.accelerate()
    race_car.accelerate()
    current_speed = 30
    assert race_car.current_speed == current_speed


def test_apply_brake_when_car_is_at_rest(race_car):
    race_car.apply_brakes()
    current_speed = 0
    assert race_car.current_speed == current_speed

def test_apply_brake_when_car_is_at_motion_when_less_than_half_of_max_speed(race_car):
    race_car.start_engine()
    race_car.accelerate()
    race_car.apply_brakes()
    race_car.apply_brakes()
    race_car.apply_brakes()
    current_speed = 1
    assert race_car.current_speed == current_speed

def test_apply_brake_when_car_is_at_motion_when_more_than_half_of_max_speed(race_car):
    race_car.start_engine()
    race_car.accelerate()
    race_car.accelerate()
    race_car.apply_brakes()
    current_speed = 17
    nitro = 10
    assert race_car.current_speed == current_speed
    assert race_car.nitro == nitro

def test_nitro_when_car_started(race_car):
    race_car.start_engine()
    nitro = 0
    assert race_car.nitro == nitro

def test_apply_brake_while_current_speed_falls_less_than_zero(race_car):
    race_car.start_engine()
    race_car.accelerate()
    race_car.apply_brakes()
    race_car.apply_brakes()
    race_car.apply_brakes()
    race_car.apply_brakes()
    race_car.apply_brakes()
    current_speed = 0
    assert race_car.current_speed == current_speed

def test_apply_brake_while_current_speed_equal_to_zero(race_car3):
    race_car3.start_engine()
    race_car3.accelerate()
    race_car3.apply_brakes()
    current_speed = 0
    assert race_car3.current_speed == current_speed

def test_sound_horn_when_car_is_at_rest(race_car, capfd):
    race_car.sound_horn()
    output = capfd.readouterr()
    assert output.out == "Start the engine to sound_horn\n"


def test_sound_horn_when_car_is_at_motion(race_car, capfd):
    race_car.start_engine()
    race_car.sound_horn()
    output = capfd.readouterr()
    assert output.out == "Peep Peep\nBeep Beep\n"


def test_stop_engine_when_engine_is_started(race_car):
    race_car.start_engine()
    race_car.stop_engine()
    is_engine_started = False
    assert race_car.is_engine_started == is_engine_started

def test_stop_engine_when_engine_is_already_stopped(race_car):
    race_car.stop_engine()
    is_engine_started = False
    assert race_car.is_engine_started == is_engine_started

def test_stop_engine_when_multiple_object_engines_are_started(race_car, race_car2):
    #arrange
    race_car2.start_engine()
    race_car.start_engine()
    #act
    race_car.stop_engine()
    is_engine_started = True
    #assert
    assert race_car2.is_engine_started == is_engine_started

def test_stop_engine_when_engine_is_in_motion(race_car):
    #arrange
    race_car.start_engine()
    race_car.accelerate()
    #act
    race_car.stop_engine()
    is_engine_started = False
    #assert
    assert race_car.is_engine_started == is_engine_started
