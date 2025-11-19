import pandas as pd
import nfl_data_py as nfl

from helperFunctions import get_team_records, get_season_Results_By_team

schedules = get_season_Results_By_team(2025)
print(schedules)

#My hypothesis- to answwer these question the best pointdifferentails are probably
# going to be the best team.
top6_Teams = ['Tb', 'IND', 'LA', 'BUF', 'SF', 'SEA']

# Whihc team has the best point diffeerential this season?


team_1 = get_season_Results_By_team(2025,'TB') #14 PD
team_2 = get_season_Results_By_team(2025,'IND') # 78
team_3 = get_season_Results_By_team(2025, 'LA')
team_4 = get_season_Results_By_team(2025, 'BUF')
team_5 = get_season_Results_By_team(2025, 'SF')
team_6 = get_season_Results_By_team(2025, 'SEA')

print(team_1)
print(team_2)
print(team_3)
print(team_4)
print(team_5)
print(team_6)
