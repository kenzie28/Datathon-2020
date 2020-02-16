import pandas as pd
import numpy as np

# Load all datasets
y15 = pd.read_csv("original_15.csv")
y16 = pd.read_csv("original_16.csv")
y17 = pd.read_csv("original_17.csv")
y18 = pd.read_csv("original_18.csv")
y19 = pd.read_csv("original_19.csv")
y20 = pd.read_csv("original_20.csv")
teams_leagues = pd.read_csv("teams_and_leagues.csv")

# Place datasets into a list for convenience
all_years = [y15, y16, y17, y18, y19, y20]

# Used to keep track of the year
i = 15
for year in all_years:
    # Calculate the fifa's predicted growth
    year["predicted_growth"] = year["potential"] - year["overall"]
    # Create column containing data on what year it is
    year["year"] = i
    # Change sofifa_id to category type to save memory space and improve runtime
    year.sofifa_id = year.sofifa_id.astype("category")

    # Seperate goalies and non-goalies
    goalkeeper = year[(year.player_positions == "GK")]
    year = year[(year.player_positions != "GK")]

    # Save each year to individual years
    filename = "players_" + str(i) + ".csv"
    filenameg = "goalkeeper_" + str(i) + ".csv"
    year.to_csv(filename)
    goalkeeper.to_csv(filenameg)
    i = i + 1

