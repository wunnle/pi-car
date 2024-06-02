from buildhat import Motor

motor_a = Motor('A')

motor_a.run_to_position(0, 10);

while True:
    print("Position: ", motor_a.get_aposition())