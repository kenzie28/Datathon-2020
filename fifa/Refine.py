import pandas as pd
import numpy as np

# Loads all datasets
players = pd.read_csv("norm_players.csv")
goalies = pd.read_csv("norm_goalies.csv")

# Selects all necessary columns
players = players[["sofifa_id", "club", "overall", "age", "player_positions", "skill_moves", "pace", "shooting", "passing", "dribbling", "defending", "physic", "predicted_growth", "year", "actual_growth"]]
goalies = goalies[["sofifa_id", "club", "overall", "age", "gk_diving", "gk_handling", "gk_kicking", "gk_reflexes", "gk_speed", "gk_positioning", "predicted_growth", "year", "actual_growth"]]

players.to_csv("refined_players.csv")
goalies.to_csv("refined_goalies.csv")
