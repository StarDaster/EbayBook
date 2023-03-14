try:
    a = input("Enter Number a: ")
    b = input("Enter Number b: ")
    a = int(a)
    b = int(b)
    print(a / b)
except (ZeroDivisionError, ValueError):
    print("Error of Enter")
