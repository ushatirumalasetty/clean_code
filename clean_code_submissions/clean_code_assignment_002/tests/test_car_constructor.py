def test_car_constructor_when_single_object_is_given(car):
    #arrange
    color = "Red"
    max_speed = 30
    acceleration = 10
    tyre_friction = 3
    #assert
    assert car.max_speed == max_speed
    assert car.acceleration == acceleration
    assert car.tyre_friction == tyre_friction
    assert car.color == color

def test_car_constructor_when_multiple_objects_are_given(car, car2):
    #arrange
    color = "Red"
    max_speed = 30
    acceleration = 10
    tyre_friction = 3
    #assert
    assert car.max_speed == max_speed
    assert car.acceleration == acceleration
    assert car.tyre_friction == tyre_friction
    assert car.color == color
    #arrange
    color = "blue"
    max_speed = 50
    acceleration = 20
    tyre_friction = 4
    #assert
    assert car2.max_speed == max_speed
    assert car2.acceleration == acceleration
    assert car2.tyre_friction == tyre_friction
    assert car2.color == color
