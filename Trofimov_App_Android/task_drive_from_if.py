try:
    speed = int(input("Enter speed a driver: "))
    if (0 < speed <= 60):
        print("Normal speed")
    if speed == 0:
        print("A car is stop")
    if speed < 0:
        print("Error complex Velue")
    if (0 != speed > 60):
        print(f"That speed Hight is {speed} > 60")

except (ZeroDivisionError, ValueError):
    print("Error Please Enter number:")
