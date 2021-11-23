import csv
from os import fstat
import plotly.figure_factory
import statistics
import pandas as pd

df = pd.read_csv("height-weight.csv")
heightlist = df["Height(Inches)"].tolist()
weightlist = df["Weight(Pounds)"].tolist()

meanheight = statistics.mean(heightlist)
medianheight = statistics.median(heightlist)
modeheight = statistics.mode(heightlist)
stddev = statistics.stdev(heightlist)
print(meanheight, medianheight, modeheight, stddev)

# first standard deviation
fstart = meanheight - stddev
fend = meanheight + stddev
print(fstart, fend)

list_of_heightdata_in_first_stdev = []
for data in heightlist:
    if data >= fstart and data <= fend:
        list_of_heightdata_in_first_stdev.append(data)

percent_of_heightdata_in_first_stdev = len(list_of_heightdata_in_first_stdev)/len(heightlist)
print(percent_of_heightdata_in_first_stdev)


# second standard deviation
sstart = meanheight - 2 * stddev
send = meanheight + 2 * stddev

list_of_heightdata_in_second_stdev = []
for data in heightlist:
    if data >= sstart and data <= send:
        list_of_heightdata_in_second_stdev.append(data)

percent_of_heightdata_in_second_stdev = len(list_of_heightdata_in_second_stdev)/len(heightlist)
print(percent_of_heightdata_in_second_stdev)

meanweight = statistics.mean(weightlist)
medianweight = statistics.median(weightlist)
modeweight = statistics.mode(weightlist)
stddevweight = statistics.stdev(weightlist)
print(meanweight, medianweight, modeweight, stddevweight)

# first standard deviation
fstart = meanweight - stddevweight
fend = meanweight + stddevweight
print(fstart, fend)

list_of_weightdata_in_first_stdev = []
for data in weightlist:
    if data >= fstart and data <= fend:
        list_of_weightdata_in_first_stdev.append(data)

percent_of_weightdata_in_first_stdev = len(list_of_weightdata_in_first_stdev)/len(weightlist)
print(percent_of_weightdata_in_first_stdev)

# second standard deviation
sstart = meanweight - 2 * stddevweight
send = meanweight + 2 * stddevweight

list_of_weightdata_in_second_stdev = []
for data in weightlist:
    if data >= sstart and data <= send:
        list_of_weightdata_in_second_stdev.append(data)

percent_of_weightdata_in_second_stdev = len(list_of_weightdata_in_second_stdev)/len(weightlist)
print(percent_of_weightdata_in_second_stdev)

#property : 68% of data values are going to lie within the first standard deviation 
#property :95% of data values are going to lie within the second standard deviation 
