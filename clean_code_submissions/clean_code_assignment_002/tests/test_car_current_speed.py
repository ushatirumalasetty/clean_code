def test_current_speed_to_zero_for_newly_created_car(car):
    #arrange
    current_speed = 0
    #act
    # assert
    assert car.current_speed == current_speed

def test_current_speed_to_zero_even_after_engine_start(car):
    #arrange
    current_speed = 0
    #act
    car.start_engine()
    #assert
    assert car.current_speed == current_speed
