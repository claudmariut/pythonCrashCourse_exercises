import matplotlib.pyplot as plt
import numpy as np

squares = np.array([0, 1, 4, 9, 16, 25])
# fig represents the entire figure or collection of plots.
# ax represents a single plot in the figure. It is a variable
fig, ax = plt.subplots()
# Using a single plot, represent "squares"
ax.plot(squares, "r--")
# Show the plot. By default, x values are integers starting fom 0.
plt.show()


