import pandas as pd
import numpy as np

data = pd.read_csv("refined_players.csv")

data = data.groupby("club").sum()

data = data[["actual_growth", "year"]]

data.to_csv("club_growth.csv")