from django.db import models
import numpy
import matplotlib.pyplot as pyplot
import numpy_hist_io
import csv
import os


class ArrivalProbabilities(models.Model):
    arrivalProbId = models.IntegerField(primary_key=True)
    binEdge = models.FloatField(null=False)
    binEntry = models.FloatField(null=True)

    # # Create some bin edges.
    bin_edges = []
    offset = 4.5
    for i in range(6):
        bin_edges.append(offset+i)

# Add some entries.
# Update these are percentages for probability times - in preparation for the charging times
    n_bins = len(bin_edges)-1
    bin_entries = [0.]*n_bins
    bin_entries[0] = 10  # 4.30 to 5.30pm
    bin_entries[1] = 27  # 5.30 to 6.30pm
    bin_entries[2] = 36  # 6.30 to 7.30pm
    bin_entries[3] = 22  # 7.30 to 8.30pm
    bin_entries[4] = 5  # 8.30 to 9.30pm
    hist = (numpy.array(bin_entries), numpy.array(bin_edges))


def hist_from_csv(file_name: str):
    """ 
    A function to read a numpy histogram from a CSV file.
    """
    input_file = open(file_name, 'r', newline='')
    csv_reader = csv.reader(input_file)
    bin_entries = []
    bin_edges = []
    for row in csv_reader:
        if csv_reader.line_num == 1:
            if row[0] != 'bin entries' or row[1] != 'bin edges':
                return None
        try:
            float_value = float(row[0])
            bin_entries.append(float_value)
        except ValueError:
            pass

        try:
            float_value = float(row[1])
            bin_edges.append(float_value)
        except ValueError:
            pass

    input_file.close()
    return (numpy.array(bin_entries), numpy.array(bin_edges))
