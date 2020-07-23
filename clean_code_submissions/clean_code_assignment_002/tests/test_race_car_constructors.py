def test_race_car_constructor_when_single_object_is_given(race_car):
    #arrange
    color = "Red"
    max_speed = 30
    acceleration = 10
    tyre_friction = 3
    #assert
    assert race_car.max_speed == max_speed
    assert race_car.acceleration == acceleration
    assert race_car.tyre_friction == tyre_friction
    assert race_car.color == color

def test_race_car_constructor_when_multiple_objects(race_car, race_car2):
    #arrange
    color = "Red"
    max_speed = 30
    acceleration = 10
    tyre_friction = 3
    #assert
    assert race_car.max_speed == max_speed
    assert race_car.acceleration == acceleration
    assert race_car.tyre_friction == tyre_friction
    assert race_car.color == color
    #arrange
    color = "blue"
    max_speed = 50
    acceleration = 20
    tyre_friction = 4
    #assert
    assert race_car2.max_speed == max_speed
    assert race_car2.acceleration == acceleration
    assert race_car2.tyre_friction == tyre_friction
    assert race_car2.color == color
