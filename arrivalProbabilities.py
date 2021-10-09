from django.db import models
import csv
import os
import numpy


class ArrivalProbabilities(models.Model):
    arrivalProbId = models.IntegerField(primary_key=True)
    binEdge = models.FloatField(null=False)
    binEntry = models.FloatField(null=True)
    hist = (numpy.array([]), numpy.array([]))


# Below is code for reference
# import numpy
# import numpy_hist_io

# """
# A program to demonstrate forming a numpy histogram from
# data values.
# """

# # Create some bin edges.
# bin_edges = []
# offset = 4.5
# for i in range(6):
#     bin_edges.append(offset+i)

# # Add some entries.
# # Update these are percentages for probability times - in preparation for the charging times
# n_bins = len(bin_edges)-1
# bin_entries = [0.]*n_bins
# bin_entries[0] = 10  # 4.30 to 5.30pm
# bin_entries[1] = 27  # 5.30 to 6.30pm
# bin_entries[2] = 36  # 6.30 to 7.30pm
# bin_entries[3] = 22  # 7.30 to 8.30pm
# bin_entries[4] = 5  # 8.30 to 9.30pm

# # Create the histogram data tuple.
# hist = (numpy.array(bin_entries), numpy.array(bin_edges))

# # Save the histogram as a PNG file.
# numpy_hist_io.hist_to_plot(hist, "times.png")

# # Save the histogram as a CSV file.
# numpy_hist_io.hist_to_csv(hist, "times.csv")
