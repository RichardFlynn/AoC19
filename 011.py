import sys

import math

total=0

for i in sys.stdin:
    total+=math.floor(int(i)/3)-2
    print(total)
