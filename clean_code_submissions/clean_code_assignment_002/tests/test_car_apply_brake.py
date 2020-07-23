def apply_brake_when_car_is_at_rest(car):
    #arrange
    current_speed = 0
    #act
    car.apply_brakes()
    #assert
    assert car.current_speed == current_speed

def apply_brake_when_car_current_speed_is_less_than_tyre_friction(car):
    #arrange
    car.start_engine()
    car.accelerate()
    car.apply_brakes()
    car.apply_brakes()
    car.apply_brakes()
    current_speed = 0
    #act
    car.apply_brakes()
    #assert
    assert car.current_speed == current_speed

def test_apply_brake_when_car_current_speed_is_more_than_tyre_friction(car):
    #arrange
    car.start_engine()
    car.accelerate()
    current_speed = 7
    #act
    car.apply_brakes()
    #assert
    assert car.current_speed == current_speed

def test_apply_brake_when_car_current_speed_is_equal_to_tyre_friction(car3):
    #arrange
    car3.start_engine()
    car3.accelerate()
    current_speed = 0
    #act
    car3.apply_brakes()
    #assert
    assert car3.current_speed == current_speed

def test_apply_brake_with_different_acceleration_current_speed_more_than_tyre_friction(car):
    #arrange
    car.start_engine()
    car.accelerate()
    car.accelerate()
    current_speed = 17
    #act
    car.apply_brakes()
    #assert
    assert car.current_speed == current_speed
