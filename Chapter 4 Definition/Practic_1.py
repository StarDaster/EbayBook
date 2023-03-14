""""
def f(x):
    return x + 2
z = f(11)
if z == 12:
    print(f"{z} equal 12")
else:
    print(f"{z} not equal 12")
    """""

"""
def f(x, y, z):
    return x + y + z


result = f(11, 22, 33)
print(result)
"""

"""
def f():
    z = 1 + 1 + 1


result = f()
print(result)
"""


age = input("Enter Age: ")
int_age = int(age)

if int_age < 34:
    print("You are Young")
else:
    print("Sorry Bro you are Old")
