import pandas as pd
import numpy as np

data = pd.read_csv("refined_players.csv")

data = data.groupby(["club", "year"]).mean().reset_index()

data.actual_growth = data.actual_growth.astype(float)

data["year"] = data.year.astype(int) + 2000

data.year = data.year.astype(str)

data.year = "01/01/" + data.year

data = data[["club", "year", "actual_growth"]]

data.to_csv("club_growth.csv")