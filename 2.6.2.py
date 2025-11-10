from math import *
def aroundx(x,y,z,theta):
    theta *= pi/180
    x = x
    y = y*cos(theta) - z*sin(theta)
    z = y*sin(theta) + z*cos(theta)
    return x,y,z

def aroundy(x,y,z,theta):
    theta *= pi/180
    x = x*cos(theta) + z*sin(theta)
    y = y
    z = -x*sin(theta) + z*cos(theta)
    return x,y,z

def aroundz(x,y,z,theta):
    theta *= pi/180
    x = x*cos(theta) - y*sin(theta)
    y = x*sin(theta) + y*cos(theta)
    z = z
    return x,y,z

while True:
    x = float(input("x = "))
    y = float(input("y = "))
    z = float(input("z = "))
    print("\n")
    print("'x' for x axis")
    print("'y' for y axis")
    print("'z' for z axis")
    print("\n")
    choice = input("Around which axis: ")
    # theta = float(input("What angle (Radians):"))
    theta = 90
    if choice == "x":
        print(aroundx(x,y,z,theta))
    elif choice == "y":
        print(aroundy(x,y,z,theta))
    elif choice == "z":
        print(aroundz(x,y,z,theta))
    else:
        print("Try again")
        break