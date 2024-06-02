import evdev

from buildhat import Motor
from numpy import interp

motor_a = Motor('A')

max = 65553.5
min = 0

output_max = 90
output_min = -90

degrees = 0

prev_target_angle = 0

print(f"max: {max}")

print(f"interval: {motor_a.interval}")

motor_a.run_to_position(0, 10);

for event in evdev.InputDevice("/dev/input/event8").read_loop():
    if event.type == evdev.ecodes.EV_ABS:
        if event.code == evdev.ecodes.ABS_X:
            print(f"Left analog stick: {event.value}")
            
            if(0 < event.value < (max / 2)):
                print("NW")
            if(max > event.value > (max / 2)):
                print("NE")
            
                    
            new_angle = round((event.value / max) * (output_max * 2)) - output_max
            print(f"new angle: {new_angle}, prev target angle: {prev_target_angle}")
            
            if(abs(prev_target_angle - new_angle) > 20):
                motor_a.run_to_position(new_angle, 50, False)
               
            prev_target_angle = new_angle
            
            
            
            
