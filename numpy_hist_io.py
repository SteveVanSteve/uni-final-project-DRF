import csv
import matplotlib.pyplot as pyplot
import numpy


def hist_bin_centres(numpy_hist: tuple):
    """
    A function to return the bin centres from a numpy histogram.
    """
    bin_entries = numpy_hist[0]
    bin_edges = numpy_hist[1]
    n_bins = len(bin_entries)
    bin_centres = []
    bin_widths = []
    for i in range(n_bins):
        bin_width = bin_edges[i+1] - bin_edges[i]
        bin_widths.append(bin_width)
        bin_centre = bin_edges[i] + bin_width*0.5
        bin_centres.append(bin_centre)
    return (bin_centres, bin_widths)


def normalised_entries(numpy_hist: tuple):
    """
    A function to return normalised entries of a numpy histogram.
    """
    bin_entries = []
    bin_entries += list(numpy_hist[0])
    total = sum(bin_entries)
    for i in range(len(bin_entries)):
        bin_entries[i] /= total
    return bin_entries


def hist_to_plot(numpy_hist: tuple, file_name: str):
    """ 
    A function to write a numpy histogram to a png file.
    """
    bin_entries = numpy_hist[0]
    (bin_centres, bin_widths) = hist_bin_centres(numpy_hist)
    pyplot.bar(bin_centres, bin_entries, bin_widths)
    pyplot.savefig(file_name)
    pyplot.close()


def hist_to_csv(numpy_hist: tuple, file_name: str):
    """ 
    A function to write a numpy histogram to a CSV file.
    """
    output_file = open(file_name, 'w', newline='')
    csv_writer = csv.writer(output_file)
    csv_writer.writerow(['bin entries', 'bin edges'])

    bin_entries = numpy_hist[0]
    bin_edges = numpy_hist[1]
    n_bins = len(bin_entries)

    for i in range(n_bins+1):
        if i == n_bins:
            csv_writer.writerow(["", bin_edges[i]])
            continue
        csv_writer.writerow([bin_entries[i], bin_edges[i]])
    output_file.close()

# reading numpy histogram from csv - I need to do this but from a database - that database
# could contain the pasted in csv values


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
