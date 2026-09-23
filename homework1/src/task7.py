import matplotlib.pyplot as plt
import numpy as np

print("This file teaches you how to use matplot. Make sure its installed.\nUse 'pip3 install matplotlibto achieve this.")

print("We are going to plot a simple graph. When are you coding you write, \nxpoints = np.array([value1, value2]) to assign x values")
print("and ypoints = np.array([value1, value2]) to assign y values\n") 

x1 = int(input("Enter in first x value: "))
x2 = int(input("Enter in second x value: "))
y1 = int(input("Enter in first y value: "))
y2 = int(input("Enter in second y value: "))


xpoints = np.array([x1, x2])
ypoints = np.array([y1, y2])

print("Sucess! This is the code you write to show the final result:")
print("plt.plot(xpoints, ypoints) plots the points on the graph")
print("and plt.savefig('plots/my_plot.png') saves the plot to a directory named plots and names it my_plot.png")

plt.plot(xpoints, ypoints)
plt.savefig("plots/my_plot.png")