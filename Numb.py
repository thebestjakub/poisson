import math  # For e and factorial
import random  # Generate random stuff
import os


mean = int(input("Enter the mean: "))
trials = int(input("How many numbers do you want? "))

po = lambda x: math.e**(-mean) * (mean**x)/math.factorial(x)


def cumulative_compare():
    cumulative = random.random()
    current = 0
    sum_to_current = 0

    while True:
        sum_to_current += po(current)
        if sum_to_current <= cumulative:
            current += 1
        else:
            return(current)


def simulate():
    po_lice = []
    for i in range(trials + 1):
        po_lice.append(cumulative_compare())
    return(po_lice)


def chi_squared(trials, observed):
    sum_chi = 0

    for i in range(max(observed) + 1):
        theorectical = po(i) * trials
        actual = po_lice.count(i)
        difference = theorectical - actual
        sum_chi += difference**2 / theorectical

    message = "Chi squared: {} Degrees of freedom: {}."
    print(message.format(str(sum_chi)[:5], max(observed)))
    return(str(sum_chi)[:5])


def graph(data):
    FileHandle = open("Data.txt", "w")
    FileHandle.write(str(mean) + " " + str(trials) + " \n")
    for i in po_lice:
        FileHandle.write(str(i) + ",")
    FileHandle.close()

    os.startfile("Graphing.py")


if __name__ == '__main__':
    po_lice = simulate()
    # chi_squared(trials, po_lice)
    graph(po_lice)
