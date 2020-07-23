def test_accelerate_when_car_engine_is_not_started(car):
    #arrange
    current_speed = 0
    #act
    car.accelerate()
    #assert
    assert car.current_speed == current_speed

def test_accelerate_with_different_acceleration_when_engine_not_started(car):
    #arrange
    current_speed = 0
    car.accelerate()
    #act
    car.accelerate()
    #assert
    assert car.current_speed == current_speed

def test_accelerate_car(car):
    #arrange
    car.start_engine()
    current_speed = 10
    #act
    car.accelerate()
    #assert
    assert car.current_speed == current_speed

def test_accelerate_car_with_different_acceleration(car):
    #arrange
    car.start_engine()
    car.accelerate()
    current_speed = 20
    #act
    car.accelerate()
    #assert
    assert car.current_speed == current_speed

def test_accelerate_car_more_than_max_limit(car):
    #arrange
    car.start_engine()
    car.accelerate()
    car.accelerate()
    car.accelerate()
    current_speed = 30
    #act
    car.accelerate()
    #assert
    assert car.current_speed == current_speed

def test_accelerate_car_with_different_acceleration_more_than_max_limit(car):
    #arrange
    car.start_engine()
    car.accelerate()
    car.accelerate()
    car.accelerate()
    car.accelerate()
    current_speed = 30
    #act
    car.accelerate()
    #assert
    assert car.current_speed == current_speed
