import pandas as pd
import numpy as np

# Loads all datasets
players = pd.read_csv("all_players.csv")
goalies = pd.read_csv("all_goalies.csv")

# Places all columns to be normalized into a list
player_columns = ["overall", "age", "skill_moves", "pace", "shooting", "passing", "dribbling", "defending", "physic", "predicted_growth"]
goalie_columns = ["overall", "age", "gk_diving", "gk_handling", "gk_kicking", "gk_reflexes", "gk_speed", "gk_positioning", "predicted_growth"]

# Iterate through each column and calculate the normalized value
for col in player_columns:
    s = "" + col
    print(s)
    print("mean: ", players[col].mean())
    print("std: ", players[col].std())
    players[col] = (players[col] - players[col].mean()) / players[col].std()


for col in goalie_columns:
    goalies[col] = (goalies[col] - goalies[col].mean()) / goalies[col].std()

# Saves dataset
players.to_csv("norm_players.csv")
goalies.to_csv("norm_goalies.csv")
