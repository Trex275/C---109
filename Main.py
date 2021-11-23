import random
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go

sum = []
for i in range(1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    sum.append(dice1+dice2)

mean1 = statistics.mean(sum)
median1 = statistics.median(sum)
mode1 = statistics.mode(sum)
stdev1 = statistics.stdev(sum)

print("Mean: ", mean1)
print("Median: ", median1)
print("Mode: ", mode1)
print("Standard deviaiton: ", stdev1)

fig = ff.create_distplot([sum], ["Result"], show_hist= False)
fig.add_trace(go.Scatter(x=[mean1, mean1], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[median1, median1], y=[0, 0.17], mode="lines", name="MEDIAN"))
fig.add_trace(go.Scatter(x=[mode1, mode1], y=[0, 0.17], mode="lines", name="MODE"))
fig.show()