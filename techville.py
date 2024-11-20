def start_engine():
    print("starting engine")

def move_forward():
    print("moving forward")

def turn(direction):
    print(f"turning {direction}")

def follow_roundabout(exit_number):
    print("entering the roundabout")
    print(f"taking exit number {exit_number} from the roundabout")

def stop_engine():
    print("stopping engine")

#start at Techville City Center
#Based on the desired destination, navigate the car using the functions.
#The direct routes: library, tech park, and a roundabout
#Roundabout locations:
#1st Exit: hospital
#2nd Exit: mall
#3rd Exit: airport
#4th Exit: university or stadium

start_engine()
destination = input("Where do you want to go? ")
arrival = destination

if destination == "library":
    move_forward()
    turn("left")
    print(f"We have arrived at the {arrival}")
elif destination == "tech park":
    move_forward()
    turn("right")
    print(f"We have arrived at the {arrival}")
elif destination == "hospital":
    move_forward()
    follow_roundabout(1)
    print(f"We have arrived at the {arrival}")
elif destination == "mall":
    move_forward()
    follow_roundabout(2)
    move_forward()
    turn("right")
    print(f"We have arrived at the {arrival}")
elif destination == "airport":
    move_forward()
    follow_roundabout(3)
    print(f"We have arrived at the {arrival}")
elif destination == "university" or destination == "stadium":
    move_forward()
    follow_roundabout(4)
    move_forward()
    if destination == "university":
        turn("left")
        print(f"We have arrived at the {arrival}")
    else:
        turn("right")
        print(f"We have arrived at the {arrival}")
else:
    print("invalid destination")