import math
from random import random
from multiprocessing import Pool
from time import clock, time

"""
A more experemental approach (not using formula)
Not sure if the distribution output is actually poisson
"""

num_points = int(input("Enter the number of points to simulate: "))
trials = int(input("Enter number of trials: "))
mean = int(input("Enter the mean: "))

def find_num(r):
    upper_bound = mean/num_points
    total = 0
    for i in range(num_points):
        if random() < upper_bound:
            total += 1
    return total

def est_time():
    t = time()
    for _ in range(5):
        find_num(0)
    dt = time() - t
    return dt * trials / 5

p = Pool()
print("Estimated time using single core:", est_time(), "seconds")
t = time()
totals = p.map(find_num, (_ for _ in range(trials)))
print("Actual time: ", time()-t, "seconds")

for i in range(1+max(totals)):
    print(totals.count(i))
