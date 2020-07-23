def test_start_engine(car):
    #arrange
    is_engine_started = True
    #act
    car.start_engine()
    #assert
    assert car.is_engine_started == is_engine_started

def test_start_engine_when_engine_is_started_twice(car):
    #arrange
    is_engine_started = True
    car.start_engine()
    #act
    car.start_engine()
    #assert
    assert car.is_engine_started == is_engine_started
