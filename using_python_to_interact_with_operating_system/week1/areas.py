# Creating modules
# To calculate areas
import math
# Triangle area
def triangle(base, height):
    return (base * height) / 2
# Rectangle area
def rectangle(base, height):
    return base * height
# Circle area
def circle(radius):
    return math.pi*(radius**2)
# You can then import this file on the powershell