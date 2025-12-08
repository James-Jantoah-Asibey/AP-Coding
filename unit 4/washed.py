from helperFunctions import get_season_totals_by_position, plot_position_stat_bar, plot_player_stat_by_week, get_player_stats

# 1. What 4 stats makes a player washed? 
'1. For a player to have been determined washed, means they have significantly declined from their peak performance. '
'Usually over time, and age. Some indicators could be health conditions, how many games theyve played, and even their amount of'
'relevancy.I chose these metrics because ofd hgow sports player are valued and what they do in their time playing sports.'

# Get all player stats from 2024
qbStats= get_season_totals_by_position(2024,'Miles Sanders')
print(qbStats)

# 2. Why is this player washed? 
'2. Miles Sanders is washed because he has endured a series of injuries over the years in the nfl.'


RussStats = get_player_stats(2024,'Russell','Wilson')

#Line graph of Russ stats for 2024
plot_player_stat_by_week(2024, 'Russell','Wilson',"passing_yards", save_path='Jalen Hurts Passing Yards 2024')
