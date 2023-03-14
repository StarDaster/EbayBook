def convert():
    return float(input("Enter Float: "))


try:
    print(convert())
except ValueError:
    print("Not can be Translate to Float")


