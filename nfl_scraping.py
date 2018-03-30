from selenium.webdriver import (Chrome, Firefox)
import pandas as pd
from itertools import chain
from collections import OrderedDict
import matplotlib.pyplot as plt
%matplotlib inline

browser = Chrome()

url = "http://www.espn.com/nfl/statistics/player/_/stat/rushing/year/2015"

browser.get(url)

sel = "tr.oddrow"
odd_players = browser.find_elements_by_css_selector(sel)

odd_players_text = [player.text for player in odd_players]

sel = "tr.evenrow"
even_players = browser.find_elements_by_css_selector(sel)

even_players_text = [player.text for player in even_players]

len(odd_players_text) == len(even_players_text)

raw_stats = []
def combine_even_odd_lines(raw_stats, odd_players_text,
                           even_players_text):
    '''Takes in a list of players that have been already
    been sorted by evens and odds and adds the odd players
    and even players to the final list'''
    for i in range(len(odd_players_text)):
        raw_stats.append(odd_players_text[i])
        raw_stats.append(even_players_text[i])
    return raw_stats

raw_stats = combine_even_odd_lines(raw_stats, 
                                    odd_players_text,
                                    even_players_text)

final_stats = []
raw_stats

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def clean_rushing_stats(line):
    '''Takes in the raw_stats of players (list) and
    the continuous dict of final_stats and returns the 
    updated finalized dict'''
    curr_char_idx = 0
    while line[curr_char_idx] not in alphabet:
        curr_char_idx += 1
    name = ''
    while line[curr_char_idx] != ',':
        name += line[curr_char_idx]
        curr_char_idx += 1
    curr_char_idx += 2
    position = line[curr_char_idx:curr_char_idx + 2]
    curr_char_idx += 3
    team = ''
    while line[curr_char_idx] != ' ':
        team += line[curr_char_idx]
        curr_char_idx += 1
    curr_char_idx += 1
    stats = ['','','','','','','','','']
    for i in range(len(stats)):
        while curr_char_idx < len(line) and line[curr_char_idx] != ' ':
            stats[i] += line[curr_char_idx]
            curr_char_idx += 1
        curr_char_idx += 1
    return OrderedDict([('player_name', name), ('position', position), ('team', team), ('att', int(stats[0])), ('yds', int(stats[1].replace(',',''))),
            ('yds_a', float(stats[2])), ('long', int(stats[3])), ('twenty_plus', int(stats[4])), ('td', int(stats[5])),
            ('yds_g', float(stats[6])), ('fumb', int(stats[7])), ('first_down', int(stats[8]))])



dict_of_stats = [clean_rushing_stats(player) for player in raw_stats]

df1 = pd.DataFrame(dict_of_stats)

df1

browser = Chrome()

url = "http://www.espn.com/nfl/statistics/player/_/stat/rushing/sort/rushingYards/year/2015/qualified/false/count/41"

browser.get(url)

sel = "tr.oddrow"
odd_players = browser.find_elements_by_css_selector(sel)

odd_players_text = [player.text for player in odd_players]

sel = "tr.evenrow"
even_players = browser.find_elements_by_css_selector(sel)

even_players_text = [player.text for player in even_players]

len(odd_players_text) == len(even_players_text)

raw_stats2 = []

raw_stats2 = combine_even_odd_lines(raw_stats2, 
                                    odd_players_text,
                                    even_players_text)

final_stats = []


dict2 = [clean_rushing_stats(player) for player in raw_stats2]
df2 = pd.DataFrame(dict2)

df_merge = [df1,df2]

df_final = pd.concat(df_merge, ignore_index=True)
# Rows 1-80



url = "http://www.espn.com/nfl/statistics/player/_/stat/rushing/sort/rushingYards/year/2015/qualified/false/count/81"

browser.get(url)

sel = "tr.oddrow"
odd_players = browser.find_elements_by_css_selector(sel)

odd_players_text = [player.text for player in odd_players]

sel = "tr.evenrow"
even_players = browser.find_elements_by_css_selector(sel)

even_players_text = [player.text for player in even_players]

raw_stats2 = combine_even_odd_lines(raw_stats2, 
                                    odd_players_text,
                                    even_players_text)

dict2 = [clean_rushing_stats(player) for player in raw_stats2]
df2 = pd.DataFrame(dict2)

df_merge = [df_final,df2]

df_final = pd.concat(df_merge, ignore_index=True)
# Rows 1-80



'''import time
import random
while True:
    time.sleep(10 + random.random() * 10)
    next_button = browser.find_element_by_css_selector("div.jcarousel-next")
    thing_below_button = browser.find_element_by_css_selector("div.OUTBRAIN")
    thing_below_button.location_once_scrolled_into_view
    next_button.click()
    url = browser.current_url
    browser.get(url)
    sel = "tr.oddrow"
    odd_players = browser.find_elements_by_css_selector(sel)
    odd_players_text = [player.text for player in odd_players]
    sel = "tr.evenrow"
    even_players = browser.find_elements_by_css_selector(sel)
    even_players_text = [player.text for player in even_players]
    combine_even_odd_lines([], odd_players, even_players)
    raw_stats = combine_even_odd_lines(raw_stats, 
                                    odd_players_text,
                                    even_players_text)
    print(raw_stats)
    dict_of_stats = [clean_rushing_stats(player) for player in raw_stats]
    df1 = pd.DataFrame(dict_of_stats)
    df_merge = [df_final, df1]
    df_final = pd.concat(df_merge, ignore_index=True)'''

fixed = df_final.drop_duplicates(subset=['player_name'])



fixed[fixed['player_name'] == 'Derek Carr']

browser = Chrome()



url = "http://www.espn.com/nfl/statistics/player/_/stat/rushing/sort/rushingYards/year/2015/qualified/false/count/121"

browser.get(url)

sel = "tr.oddrow"
odd_players = browser.find_elements_by_css_selector(sel)

odd_players_text = [player.text for player in odd_players]

sel = "tr.evenrow"
even_players = browser.find_elements_by_css_selector(sel)

even_players_text = [player.text for player in even_players]

raw_stats2 = combine_even_odd_lines(raw_stats2, 
                                    odd_players_text,
                                    even_players_text)

dict2 = [clean_rushing_stats(player) for player in raw_stats2]
df2 = pd.DataFrame(dict2)

df_merge = [df_final,df2]

df_final = pd.concat(df_merge, ignore_index=True)
# Rows 1-80



url = "http://www.espn.com/nfl/statistics/player/_/stat/rushing/sort/rushingYards/year/2015/qualified/false/count/161"

browser.get(url)

sel = "tr.oddrow"
odd_players = browser.find_elements_by_css_selector(sel)

odd_players_text = [player.text for player in odd_players]

sel = "tr.evenrow"
even_players = browser.find_elements_by_css_selector(sel)

even_players_text = [player.text for player in even_players]

raw_stats2 = combine_even_odd_lines(raw_stats2, 
                                    odd_players_text,
                                    even_players_text)

dict2 = [clean_rushing_stats(player) for player in raw_stats2]
df2 = pd.DataFrame(dict2)

df_merge = [df_final,df2]

df_final = pd.concat(df_merge, ignore_index=True)



url = "http://www.espn.com/nfl/statistics/player/_/stat/rushing/sort/rushingYards/year/2015/qualified/false/count/201"

browser.get(url)

sel = "tr.oddrow"
odd_players = browser.find_elements_by_css_selector(sel)

odd_players_text = [player.text for player in odd_players]

sel = "tr.evenrow"
even_players = browser.find_elements_by_css_selector(sel)

even_players_text = [player.text for player in even_players]

raw_stats2 = combine_even_odd_lines(raw_stats2, 
                                    odd_players_text,
                                    even_players_text)

dict2 = [clean_rushing_stats(player) for player in raw_stats2]
df2 = pd.DataFrame(dict2)

df_merge = [df_final,df2]

df_final = pd.concat(df_merge, ignore_index=True)



url = "http://www.espn.com/nfl/statistics/player/_/stat/rushing/sort/rushingYards/year/2015/qualified/false/count/241"

browser.get(url)

sel = "tr.oddrow"
odd_players = browser.find_elements_by_css_selector(sel)

odd_players_text = [player.text for player in odd_players]

sel = "tr.evenrow"
even_players = browser.find_elements_by_css_selector(sel)

even_players_text = [player.text for player in even_players]

raw_stats2 = combine_even_odd_lines(raw_stats2, 
                                    odd_players_text,
                                    even_players_text)

dict2 = [clean_rushing_stats(player) for player in raw_stats2]
df2 = pd.DataFrame(dict2)

df_merge = [df_final,df2]

df_final = pd.concat(df_merge, ignore_index=True)

df_final = df_final.drop_duplicates(subset=['player_name'])



url = "http://www.espn.com/nfl/statistics/player/_/stat/rushing/sort/rushingYards/year/2015/qualified/false/count/281"

browser.get(url)

sel = "tr.oddrow"
odd_players = browser.find_elements_by_css_selector(sel)

odd_players_text = [player.text for player in odd_players]

sel = "tr.evenrow"
even_players = browser.find_elements_by_css_selector(sel)

even_players_text = [player.text for player in even_players]

raw_stats2 = combine_even_odd_lines(raw_stats2, 
                                    odd_players_text,
                                    even_players_text)

dict2 = [clean_rushing_stats(player) for player in raw_stats2]
df2 = pd.DataFrame(dict2)

df_merge = [df_final,df2]

df_final = pd.concat(df_merge, ignore_index=True)





url = "http://www.espn.com/nfl/statistics/player/_/stat/rushing/sort/rushingYards/year/2015/qualified/false/count/321"

browser.get(url)

sel = "tr.oddrow"
odd_players = browser.find_elements_by_css_selector(sel)

odd_players_text = [player.text for player in odd_players]

sel = "tr.evenrow"
even_players = browser.find_elements_by_css_selector(sel)

even_players_text = [player.text for player in even_players]

raw_stats2 = combine_even_odd_lines(raw_stats2, 
                                    odd_players_text,
                                    even_players_text)

dict2 = [clean_rushing_stats(player) for player in raw_stats2]
df2 = pd.DataFrame(dict2)

df_merge = [df_final,df2]

df_final = pd.concat(df_merge, ignore_index=True)

#pd.scatter_matrix(df_final)

df_final = df_final.drop_duplicates()

df_final = df_final.reset_index(drop=True)

df_final

df_final.to_csv('~/galvanize/Data/nfl/nfl_rushing_yards_data.csv')

fig, axs = plt.subplots(3, figsize=(15,15))
axs[0].scatter(df_final['yds'], df_final['yds_g'],label='Total Yards vs. Yards / Game')
axs[0].set_ylabel('Total Yards')
axs[0].set_xlabel('Yards / Game')
axs[1].scatter(df_final['yds'], df_final['td'], label='Total Yards vs. Total Touchdowns')
axs[1].set_ylabel('Total Yards')
axs[1].set_xlabel('Total Touchdowns')
axs[2].scatter(df_final['yds'], df_final['first_down'], label='Total Yards vs. Total # of First Downs')
axs[2].set_ylabel('Total Yards')
axs[2].set_xlabel('Total # of First Downs')

df_final.info()

