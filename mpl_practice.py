#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import statistics

# %%
%matplotlib inline
# %%
# Set the x-axis to a list of strings for each month.
x_axis = ["Jan", "Feb", "Mar", "April", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
# Set the y-axis to a list of floats as the total fare in US dollars accumulated for each month.
y_axis = [10.02, 23.24, 39.20, 35.42, 32.34, 27.04, 43.82, 10.56, 11.85, 27.90, 20.71, 20.09]
# Create the plot
plt.plot(x_axis, y_axis)

# %%
# Create the plot with ax.plt()
fig, ax = plt.subplots()
ax.plot(x_axis, y_axis)
# %%
# Create the plot with ax.plt()
fig = plt.figure()
ax = fig.add_subplot()
ax.plot(x_axis, y_axis)
# %%
# Create the plot with ax.plt()
ax = plt.axes()
ax.plot(x_axis, y_axis)
plt.show()
# %%
# Create the plot and add a label for the legend.
plt.plot(x_axis, y_axis, label='Boston')
# Create labels for the x and y axes.
plt.xlabel("Date")
plt.ylabel("Fare($)")
# Set the y limit between 0 and 45.
plt.ylim(0, 45)
# Create a title.
plt.title("PyBer Fare by Month")
# Add the legend.
plt.legend()
# %%
# Create the plot.
plt.plot(x_axis, y_axis, marker="*", color="blue", linewidth=2, label='Boston')
# Create labels for the x and y axes.
plt.xlabel("Date")
plt.ylabel("Fare($)")
# Set the y limit between 0 and 45.
plt.ylim(0, 45)
# Create a title.
plt.title("PyBer Fare by Month")
# Add a grid.
plt.grid()
# Add the legend.
plt.legend()
# %%
# Set the x-axis to a list of strings for each month.
x_axis = ["Jan", "Feb", "Mar", "April", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]

# Set the y-axis to a list of floats as the total fare in US dollars accumulated for each month.
y_axis = [10.02, 23.24, 39.20, 35.42, 32.34, 27.04, 43.82, 10.56, 11.85, 27.90, 20.71, 20.09]
# %%
# Create the plot
plt.bar(x_axis, y_axis)
# %%
# Create the plot.
plt.bar(x_axis, y_axis, color="green", label='Boston')
# Create labels for the x and y axes.
plt.xlabel("Date")
plt.ylabel("Fare($)")
# Create a title.
plt.title("PyBer Fare by Month")
# Add the legend.
plt.legend()
# %%
# Create the plot
plt.barh(x_axis, y_axis)
# %%
# Create the plot.
plt.barh(x_axis, y_axis)
plt.gca().invert_yaxis()
# %%
# Set the x-axis to a list of strings for each month.
x_axis = ["Jan", "Feb", "Mar", "April", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]

# Set the y-axis to a list of floats as the total fare in US dollars accumulated for each month.
y_axis = [10.02, 23.24, 39.20, 35.42, 32.34, 27.04, 43.82, 10.56, 11.85, 27.90, 20.71, 20.09]
# %%
# Create the plot with ax.plt()
fig, ax = plt.subplots()
ax.bar(x_axis, y_axis)
# %%
# Set the x-axis to a list of strings for each month.
x_axis = ["Jan", "Feb", "Mar", "April", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]

# Set the y-axis to a list of floats as the total fare in US dollars accumulated for each month.
y_axis = [10.02, 23.24, 39.20, 35.42, 32.34, 27.04, 43.82, 10.56, 11.85, 27.90, 20.71, 20.09]
# %%
plt.scatter(y_axis, x_axis, c="red", label="Chicago")
plt.title("PyBer Fare by Month")
plt.ylabel("Fare($)")
plt.xlabel("Date")
plt.gca().invert_yaxis()
plt.legend()
plt.show()
# %%
plt.scatter(x_axis, y_axis, s = [i * 3 for i in y_axis])
# %%
plt.pie(y_axis, labels=x_axis)
plt.show()
# %%
explode_values = (0, 0, 0, 0, 0, 0, 0.2, 0, 0, 0, 0, 0)
plt.pie(y_axis, explode=explode_values, labels=x_axis, autopct='%.1f%%')
#%%
# Set the x-axis to a list of strings for each month.
x_axis = ["Jan", "Feb", "Mar", "April", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]

# Set the y-axis to a list of floats as the total fare in US dollars accumulated for each month.
y_axis = [10.02, 23.24, 39.20, 35.42, 32.34, 27.04, 43.82, 10.56, 11.85, 27.90, 20.71, 20.09]
# %%
# Get the standard deviation of the values in the y-axis.
stdev = statistics.stdev(y_axis)
stdev
# %%
plt.errorbar(x_axis, y_axis, yerr=stdev, capsize=3)
# %%
fig, ax = plt.subplots()
ax.errorbar(x_axis, y_axis, yerr=stdev, capsize=3)
plt.show()
# %%
fig, ax = plt.subplots()
ax.bar(x_axis, y_axis, yerr=stdev, capsize=3)
plt.show()
# %%
plt.barh(x_axis, y_axis)
plt.xticks(np.arange(0, 51, step=5.0))
plt.gca().invert_yaxis()
# %%

# Increase the size of the plot figure.
fig, ax = plt.subplots(figsize=(8, 8))
ax.barh(x_axis, y_axis)
ax.set_xticks(np.arange(0, 51, step=5.0))

# Create minor ticks at an increment of 1.
ax.xaxis.set_minor_locator(MultipleLocator(1))
plt.show()
# %%
