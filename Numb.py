import math
import random

lba = int(input("Enter the mean: "))
po = lambda x: math.e**(-lba) * (lba**x)/math.factorial(x)


def cumulative_compare():
    cumulative = random.random()
    current = 0
    sum_thing = 0

    while True:
        sum_thing += po(current)
        if sum_thing <= cumulative:
            current += 1
        else:
            return(current)


trials = int(input("How many numbers do you want?: ")) + 1
po_lice = []

for i in range(trials):
    po_lice.append(cumulative_compare())

for i in range(max(po_lice)):
    thing = po_lice.count(i)
    print(thing)
