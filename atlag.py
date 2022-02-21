from itertools import permutations
import random
from re import X

szamok=[2,5,7,8,9,5,6,11,1,10]
print('Minimum kiválasztás elve: ')
max1=1
for x in szamok:
    if x>max1:
        max1=x
print(max1)
print(max(szamok))