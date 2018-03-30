import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

rushing_yds = pd.read_csv('~/galvanize/Data/nfl/nfl_rushing_yards_data.csv')

basic_info = pd.read_csv('/Users/elisereppond/galvanize/Data/nfl/basic_player_stats.csv')

basic_info = basic_info.drop(['Unnamed: 0'], axis=1)

rushing_yds.head()

basic_info.head()

basic_info = basic_info.rename(columns={'name': 'player_name'})

merged = pd.merge(basic_info, rushing_yds, left_on='player_name', right_on='player_name', how='outer')

merged = merged[merged.death_date.notnull() == False]

merged = merged[merged.current_team.notnull() == True]

merged = merged[merged.yds.notnull() == True]

merged = merged.drop(['death_date'], axis=1)

merged = merged.drop('player_id', axis=1)

merged = merged.drop('Unnamed: 0', axis=1)

merged = merged.drop('hof_induction_year', axis=1)

columns = merged.columns

merged['birth_date'] = pd.to_datetime(merged['birth_date'])

merged.reset_index(inplace=True)

now = pd.datetime.now()
merged['age'] = now - merged['birth_date']

merged = merged[['player_name','age','draft_team', 'current_team', 'position_x', 'weight', 'height',
                 'yds', 'birth_date', 'birth_place', 'college', 'current_salary', 'draft_position',
                 'draft_round', 'draft_team', 'draft_year', 'yds_a', 'long', 'twenty_plus', 'td',
                 'yds_g', 'fumb', 'first_down', 'high_school', 'position_y']]

merged = merged.drop('high_school', axis=1)


merged.to_csv('/Users/elisereppond/galvanize/Data/nfl/basic_and_rushing_data_2015.csv')