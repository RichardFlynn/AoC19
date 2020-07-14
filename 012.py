import sys
import math

def fuelcalc(mass):
    if mass<8:
        return 0
    return math.floor(mass/3)-2+fuelcalc(math.floor(mass/3)-2)

total=0
fuel=0

for i in sys.stdin:
    total+=fuelcalc(int(i))
    print(total)