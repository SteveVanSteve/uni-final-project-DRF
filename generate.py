from random import random
import sys
import scipy.stats
import matplotlib.pyplot as pyplot
import numpy
import numpy_hist_io
import random


"""
A program to generate numbers from a histogrammed
distribution.  The histogram is used as a probability
distribution function.
"""

# Load a histogram from a CSV file.
# EDIT - this needs changed to something that can be read from a database.
# change from csv to what will be in my db from my model structure
hist = numpy_hist_io.hist_from_csv("times.csv")
if hist is None:
    sys.exit(1)

# Create the distribution from the histogram, using linear interpolation.
# I need a loop over cars and then outside of that I need a loop over days
# the name 'hist_dist' will be whatever I like to call it
hist_dist = scipy.stats.rv_histogram(hist)

# Generate values from the interpolated inverse CDF.
# values = []
for i_day in range(1000):
    values = []  # Start of charge times.
    for i_car in range(5):
        q = random.uniform(0, 1)
        values.append(hist_dist.ppf(q))
    # Now calculate the electric current as a function of time for all 5 houses
    # assuming the five start times.

# Create a histogram to compare the generated distribution
# with the input distrubtion.
nbins = len(hist[0])
x_min = hist[1][0]
x_max = hist[1][nbins]
output_hist = numpy.histogram(values, bins=nbins, range=(x_min, x_max))

# Compare the two histograms, by overlaying the two normalised
# histograms.
(bin_centres, bin_widths) = numpy_hist_io.hist_bin_centres(hist)
entries = numpy_hist_io.normalised_entries(hist)
pyplot.bar(bin_centres, entries, bin_widths, color="blue")
entries = numpy_hist_io.normalised_entries(output_hist)
pyplot.bar(bin_centres, entries, bin_widths, color="None",
           linewidth=1, edgecolor="red", linestyle="--")
pyplot.show()
