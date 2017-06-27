import math
import random
from multiprocessing import Pool

lba = int(input("Enter the mean: "))
po = lambda x: math.e**(-lba) * (lba**x)/math.factorial(x)


def cumulative_compare(cumulative):
    current = 0
    sum_thing = 0

    while True:
        sum_thing += po(current)
        if sum_thing <= cumulative:
            current += 1
        else:
            return(current)


trials = int(input("How many numbers do you want?: ")) + 1
p = Pool()
po_lice = p.map(cumulative_compare, (random.random() for _ in range(trials)))

#for i in range(trials):
#    po_lice.append(cumulative_compare())

for i in range(max(po_lice) + 1):
    thing = po_lice.count(i)
    print(thing)
