# Code from user Zah on SO
# https://stackoverflow.com/questions/10944621/dynamically-updating-plot-in-matplotlib

import matplotlib.pyplot as plt
import numpy
import math
import time
plt.ion()

FileHandle = open("Data.txt", "r")
Data = FileHandle.read()
Mean, Trials = Data.split("\n")[0].split(" ")[0:2]
Mean, Trials = int(Mean), int(Trials)
Data = Data.split("\n")[1].split(",")[:-1]
FileHandle.close()
Data = [int(i) for i in Data]

po = lambda x: math.e**(-Mean) * (Mean**x)/math.factorial(x)


def chi_squared(trials, observed):
    sum_chi = 0

    for i in range(max(observed) + 1):
        theorectical = po(i) * trials
        actual = observed.count(i)
        difference = theorectical - actual
        sum_chi += difference**2 / theorectical

    return(str(sum_chi)[:5], max(observed))


class DynamicUpdate():
    min_x = 0
    max_x = max(Data)
    message = "{} data points\nChi squared: {} with {} degrees of freedom"

    def on_launch(self):
        # Set up plot
        self.figure, self.ax = plt.subplots()
        self.lines, = self.ax.plot([], [], 'o')
        # Autoscale on unknown axis and known lims on the other
        self.ax.set_autoscaley_on(True)
        self.ax.set_xlim(self.min_x, self.max_x)
        self.ax.set_xticks(numpy.arange(0, max(Data) + 1, 1))
        self.ax.set_xlabel("Value")
        self.ax.set_ylabel("Frequency")
        # Other stuff
        self.ax.grid()

    def on_running(self, xdata, ydata):
        # Update data (with the new _and_ the old points)
        self.lines.set_xdata(xdata)
        self.lines.set_ydata(ydata)
        # Need both of these in order to rescale
        self.ax.relim()
        self.ax.autoscale_view()
        # We need to draw *and* flush
        self.figure.canvas.draw()
        self.figure.canvas.flush_events()

    # Example
    def __call__(self):
        # import numpy as np
        self.on_launch()
        xdata = [i for i in range(max(Data) + 1)]
        ydata = []
        for x in range(1, Trials + int(Trials*0.01), int(Trials*0.01)):
            ydata = [Data[0:x].count(i) for i in range(max(Data) + 1)]
            self.ax.set_title(self.message.format(x-1, chi_squared(x, Data[0:x])[0], chi_squared(x, Data[0:x])[1]))
            self.on_running(xdata, ydata)
            time.sleep(0.1)
        input("Done! ")
        return xdata, ydata


d = DynamicUpdate()
d()
