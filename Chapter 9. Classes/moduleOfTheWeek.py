from statistics import *

data = [1, 2, 2, 5, 10, 12]

# Mean. Average. To round to 2 decimal places. {:.2f}.format
print("{:.2f}".format(mean(data)))

# Mode. Most often occurrence.
print(mode(data))

# Median. Number in the middle.
print("Median: {:.2f}".format(median(data)))
print("Low median: {:.2f}".format(median_low(data)))
print("High median: {:.2f}".format(median_high(data)))

