"""
colors = ["Blue", "Green", "Yellow"]
colors[2] = "Red"
print(colors)
"""

"""
colors = ["Blue", "Green", "Yellow"]
print(colors)
item =colors.pop()
print(item)
print(colors)
"""

color1 = [3, 2, 1]
color2 = [6, 5, 4]
# color1 = list(reversed(color1))
print(list(reversed(color1)) + list(reversed(color2)))
print(*list(reversed(color1)) + list(reversed(color2)))
