try:
    day = int(input("Enter number day: "))
    if day == 7:
        print("That day is Wekeend go drive to Bicycle")
    elif day == 1:
        print("That day is Monday")
    elif day < 1 or day > 7:
        print("That day is not to be")
    else:
        print(f"The Day {day} < 7")
except (ZeroDivisionError, ValueError):
    print(" Error Please Enter number:")
