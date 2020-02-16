import pandas as pd
import numpy as np

# Load all datasets
y15 = pd.read_csv("players_15.csv", usecols=["sofifa_id", "long_name", "age", "overall", "potential", "club", "player_positions", "skill_moves", "pace", "shooting", "passing", "dribbling", "defending", "physic", "predicted_growth", "year"], engine="c")
y16 = pd.read_csv("players_16.csv", usecols=["sofifa_id", "long_name", "age", "overall", "potential", "club", "player_positions", "skill_moves", "pace", "shooting", "passing", "dribbling", "defending", "physic", "predicted_growth", "year"], engine="c")
y17 = pd.read_csv("players_17.csv", usecols=["sofifa_id", "long_name", "age", "overall", "potential", "club", "player_positions", "skill_moves", "pace", "shooting", "passing", "dribbling", "defending", "physic", "predicted_growth", "year"], engine="c")
y18 = pd.read_csv("players_18.csv", usecols=["sofifa_id", "long_name", "age", "overall", "potential", "club", "player_positions", "skill_moves", "pace", "shooting", "passing", "dribbling", "defending", "physic", "predicted_growth", "year"], engine="c")
y19 = pd.read_csv("players_19.csv", usecols=["sofifa_id", "long_name", "age", "overall", "potential", "club", "player_positions", "skill_moves", "pace", "shooting", "passing", "dribbling", "defending", "physic", "predicted_growth", "year"], engine="c")
y20 = pd.read_csv("players_20.csv", usecols=["sofifa_id", "long_name", "age", "overall", "potential", "club", "player_positions", "skill_moves", "pace", "shooting", "passing", "dribbling", "defending", "physic", "predicted_growth", "year"], engine="c")

g15 = pd.read_csv("goalkeeper_15.csv", usecols = ["sofifa_id", "long_name", "age", "overall", "potential", "club", "gk_diving", "gk_handling", "gk_kicking", "gk_reflexes", "gk_speed", "gk_positioning", "predicted_growth", "year"], engine="c")
g16 = pd.read_csv("goalkeeper_16.csv", usecols = ["sofifa_id", "long_name", "age", "overall", "potential", "club", "gk_diving", "gk_handling", "gk_kicking", "gk_reflexes", "gk_speed", "gk_positioning", "predicted_growth", "year"], engine="c")
g17 = pd.read_csv("goalkeeper_17.csv", usecols = ["sofifa_id", "long_name", "age", "overall", "potential", "club", "gk_diving", "gk_handling", "gk_kicking", "gk_reflexes", "gk_speed", "gk_positioning", "predicted_growth", "year"], engine="c")
g18 = pd.read_csv("goalkeeper_18.csv", usecols = ["sofifa_id", "long_name", "age", "overall", "potential", "club", "gk_diving", "gk_handling", "gk_kicking", "gk_reflexes", "gk_speed", "gk_positioning", "predicted_growth", "year"], engine="c")
g19 = pd.read_csv("goalkeeper_19.csv", usecols = ["sofifa_id", "long_name", "age", "overall", "potential", "club", "gk_diving", "gk_handling", "gk_kicking", "gk_reflexes", "gk_speed", "gk_positioning", "predicted_growth", "year"], engine="c")
g20 = pd.read_csv("goalkeeper_20.csv", usecols = ["sofifa_id", "long_name", "age", "overall", "potential", "club", "gk_diving", "gk_handling", "gk_kicking", "gk_reflexes", "gk_speed", "gk_positioning", "predicted_growth", "year"], engine="c")

# Save datasets into lists of goalies and non-goalies
all_years = [y15, y16, y17, y18, y19, y20]
all_goalies = [g15, g16, g17, g18, g19, g20]

# use the sofifa_id as the index and create empty "actual growth" column
for year in all_years:
    year.set_index("sofifa_id", drop=False, inplace=True, verify_integrity=True)
    year["actual_growth"] = year["overall"] - year["overall"]

for goalies in all_goalies:
    goalies.set_index("sofifa_id", drop=False, inplace=True, verify_integrity=True)
    goalies["actual_growth"] = goalies["overall"] - goalies["overall"]


# Calculate the actual growth of each player between each year
# If a player is no longer in the league next year, his data is dropped
for i in range(len(all_years)-1):
    print(i)
    for id in all_years[i]["sofifa_id"]:
        if (id in all_years[i+1]["sofifa_id"]):
            all_years[i]["actual_growth"].loc[id] = all_years[i+1].loc[id, "overall"] - all_years[i].loc[id, "overall"]
        else:
            all_years[i].drop(index=id, inplace=True, axis=0)
    
for i in range(len(all_goalies)-1):
    print(i)
    for id in all_goalies[i]["sofifa_id"]:
        if (id in all_goalies[i+1]["sofifa_id"]):
            all_goalies[i]["actual_growth"].loc[id] = all_goalies[i+1].loc[id, "overall"] - all_goalies[i].loc[id, "overall"]
        else:
            all_goalies[i].drop(index=id, inplace=True, axis=0)
    
# Concatenate the datasets throughout the years
players = pd.concat(all_years)
goalies = pd.concat(all_goalies)

# Save the dataset to csv format
players.to_csv("all_players.csv")
goalies.to_csv("all_goalies.csv")