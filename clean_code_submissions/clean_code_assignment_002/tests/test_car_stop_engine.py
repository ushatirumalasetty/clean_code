def test_stop_engine_when_car_engine_is_started(car):
    #arrange
    car.start_engine()
    is_engine_started = False
    #act
    car.stop_engine()
    #assert
    assert car.is_engine_started == is_engine_started

def test_stop_engine_when_engine_is_already_stopped(car):
    #arrange
    car.start_engine()
    car.stop_engine()
    is_engine_started = False
    #act
    car.stop_engine()
    #assert
    assert car.is_engine_started == is_engine_started

def test_stop_engine_when_car_is_running(car):
    #arrange
    car.start_engine()
    car.accelerate()
    is_engine_started = False
    #act
    car.stop_engine()
    #assert
    assert car.is_engine_started == is_engine_started
