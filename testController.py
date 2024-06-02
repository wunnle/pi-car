import evdev

from buildhat import Motor
from numpy import interp

motor_a = Motor('A')

max = 65553.5
min = 0

degrees = 0

print(f"max: {max}")

motor_a.run_to_position(0, 10);

for event in evdev.InputDevice("/dev/input/event8").read_loop():
    if event.type == evdev.ecodes.EV_ABS:
        if event.code == evdev.ecodes.ABS_X:
            print(f"Left analog stick: {event.value}")
            
            if(0 < event.value < (max / 2)):
                print("NW")
            if(max > event.value > (max / 2)):
                print("NE")
            
                    
            new_angle = round((event.value / max) * 180) - 90
            print(f"new angle: {new_angle}")
            motor_a.run_to_position(new_angle, 60, True);
            
            
            
            