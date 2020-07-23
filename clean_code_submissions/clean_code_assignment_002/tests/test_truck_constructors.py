def test_truck_constructor_for_object_creation_with_given_values(truck):
    #arrange
    color = "Red"
    max_speed = 30
    acceleration = 10
    tyre_friction = 3
    max_cargo_weight = 30
    #act
    #assert
    assert truck.max_speed == max_speed
    assert truck.acceleration == acceleration
    assert truck.tyre_friction == tyre_friction
    assert truck.color == color
    assert truck.max_cargo_weight == max_cargo_weight

def test_truck_constructor_for_multiple_objects_creation(truck, truck2):
    color = "Red"
    max_speed = 30
    acceleration = 10
    tyre_friction = 3
    max_cargo_weight = 30
    assert truck.max_speed == max_speed
    assert truck.acceleration == acceleration
    assert truck.tyre_friction == tyre_friction
    assert truck.color == color
    assert truck.max_cargo_weight == max_cargo_weight
    color = "blue"
    max_speed = 50
    acceleration = 20
    tyre_friction = 4
    max_cargo_weight = 40
    assert truck2.max_speed == max_speed
    assert truck2.acceleration == acceleration
    assert truck2.tyre_friction == tyre_friction
    assert truck2.color == color
    assert truck2.max_cargo_weight == max_cargo_weight
