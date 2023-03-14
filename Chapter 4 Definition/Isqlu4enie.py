def a():
    return int(input("Enter Number: "))


def b():
    return int(input("Enter Number: "))


try:
    print(a() / b())
except (ZeroDivisionError, ValueError):
    print("Na 0 Delitb NelbZ9 or Enter Number Please")
