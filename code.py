import pandas as pd 
import statistics 
import plotly.figure_factory as ff

df = pd.read_csv("data.csv")

print(statistics.mean(df["Avg Rating"]))
print(statistics.mode(df["Avg Rating"]))
print(statistics.median(df["Avg Rating"]))

fig = ff.create_distplot([df["Avg Rating"].tolist()], ["Avg Rating"], show_hist=False)
fig.show()