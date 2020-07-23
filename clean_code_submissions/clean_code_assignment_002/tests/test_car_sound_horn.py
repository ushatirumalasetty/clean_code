def test_sound_horn_when_car_engine_is_not_started(car, capfd):
    #arrange
    #act
    car.sound_horn()
    output = capfd.readouterr()
    #assert
    assert output.out == "Start the engine to sound_horn\n"

def test_sound_horn_when_car_engine_is_started(car, capfd):
    #arrange
    car.start_engine()
    #act
    car.sound_horn()
    output = capfd.readouterr()
    #assert
    assert output.out == "Beep Beep\n"
