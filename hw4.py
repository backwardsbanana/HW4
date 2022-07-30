import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

frame1 = pd.read_csv("olympic_medals.csv")

frame1 = frame1.loc[frame1["Year"] >= 2000]

px.parallel_categories(frame1, dimensions=["Year", "Medal", "Gender"], color="Year", color_continuous_scale=px.colors.sequential.Viridis)

#########################

frame2 = pd.read_csv("2016elections.csv")
states = ["Arkansas", "Michigan", "California", "Wisconsin"]

frame2 = frame2.loc[(frame2["state"] == states[0]) | (frame2["state"] == states[1]) | (frame2["state"] == states[2]) | (frame2["state"] == states[3])]
frame2.drop(["st", "fips", "total_vote", "vote_margin", "winner", "party", "clinton_vote", "johnson_vote", "trump_vote", "other_vote", "ev_dem", "ev_rep", "ev_oth", "census", "pct_margin", "d_points", "r_points"], axis=1, inplace=True)

frame2.plot(figsize=(15, 5), kind="bar", stacked=True, color=["blue", "red", "yellow", "grey"])
plt.xticks(plt.gca().get_xticks(), states, rotation="horizontal")
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.xlabel("States")
plt.ylabel("Percentage of Votes")
plt.title("2016 Election Results By State")
plt.show()