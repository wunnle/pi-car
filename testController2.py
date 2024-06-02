import evdev

from buildhat import Motor
from numpy import interp
from numpy import average
import time

motor_a = Motor('A')

max = 65553.5
min = 0

last_read_time = 0

previous_angle = 0
degrees = 0

print(f"max: {max}")

motor_a.run_to_position(0, 10);

def calculate_speed(current_position, new_position):
    return round((abs(new_position - current_position) / 180) * 100, 2)

for event in evdev.InputDevice("/dev/input/event8").read_loop():
    
    print("hello")
    
    
    if event.type == evdev.ecodes.EV_ABS:
        if event.code == evdev.ecodes.ABS_X:
            new_angle = round((event.value / max) * 180) - 90
            print(new_angle)
            
            current_position = motor_a.get_aposition()
            
            if(abs(new_angle - current_position) < 30):
                print("less than 30")
            else:
                            
                print(f"motor position: {current_position}")
            
                ##speed = calculate_speed(current_position, new_angle)
                
                speed = 40
            
                motor_a.run_to_position(((current_position*3 + new_angle) / 4), speed, True)
            

            
            
            
            