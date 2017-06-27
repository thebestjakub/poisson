import math  # For e and factorial
import random  # Generate random stuff
# Below two don't come standard with Python, you have to pip install them
# Needed for graphing, you can comment these and graph() out if necessary
import numpy as np  # Needed to store arrays in a form matplotlib understands
import matplotlib.pyplot as plt  # Graphing


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
    '''
    Uncomment print statements to get it to print intermediary values, but the
    formatting isn't great, if you want you can figure that one out
    '''
    sum_chi = 0

    for i in range(max(observed) + 1):
        theorectical = po(i) * trials
        actual = po_lice.count(i)
        difference = theorectical - actual
        sum_chi += difference**2 / theorectical
        # print("{} {} {} {}".format(i, theorectical, actual, difference))

    message = "The chi squared value is {} There are {} degrees of freedom."
    print(message.format(str(sum_chi)[:5], max(observed)))
    # str(sum_chi)[:5]  lazy way to do 5 sf without having to import anything


def graph(data):
    # Declare data as numpy arrays
    x = np.arange(0, max(data) + 1)
    y = np.asarray([data.count(i) for i in range(max(data) + 1)])

    # Set default size of window, can resize
    ax = plt.figure(figsize=(50, 50)).add_subplot(111)

    # Axis labels
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")
    dots, = plt.plot(y, "o", markersize=5)  # Plotting style
    plt.scatter(x, y)  # Scatter plot
    plt.ylim(ymin=0)  # Set defaust lowest y-value
    plt.xlim(xmin=0, xmax=max(data))  # default lowest x, highest x
    plt.xticks(np.arange(0, max(data)+1, 1))  # scale, 0 to max, step size 1

    # Key at top
    plt.legend([dots], ["Frequency with lambda equals {}".format(mean)])

    # Plot
    plt.show()


if __name__ == '__main__':
    po_lice = simulate()
    chi_squared(trials, po_lice)
    graph(po_lice)
