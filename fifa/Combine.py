import pandas as pd
import numpy as np

players = pd.read_csv("refined_players.csv")
goalies = pd.read_csv("refined_goalies.csv")


players.year = players.year.astype(str)

if (players.loc[10, "year"] == "15"):
    print("yes")

for i in range(len(players.age)):
    if players.loc[i, "year"] == "15":




