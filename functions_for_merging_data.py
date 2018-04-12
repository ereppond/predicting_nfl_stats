import pandas as pd
pd.set_option('display.max_columns', None)

df_2011 = pd.read_csv('../data/nfl_2011_rushing_and_receiving_stats.csv')
df_2012 = pd.read_csv('../data/nfl_2012_rushing_and_receiving_stats.csv')
df_2013 = pd.read_csv('../data/nfl_2013_rushing_and_receiving_stats.csv')
df_2014 = pd.read_csv('../data/nfl_2014_rushing_and_receiving_stats.csv')
df_2015 = pd.read_csv('../data/nfl_2015_rushing_and_receiving_stats.csv')
df_2016 = pd.read_csv('../data/nfl_2016_rushing_receiving_stats.csv')

def short_name(name):
	''''''
    for i in range(len(name)):
        if name[i] in "*+\\":
            return name[:i]

def fix_names(df):

    return df['Name'].apply(lambda x: short_name(x))

def change_in_teams(df, year_1, year_2): 

    df['diff_in_team_{}-{}'.format(year_1, year_2)] = df['Team_{}'.format(year_1)] != df['Team_{}'.format(year_2)]
    return df

def change_in_col(df, year_1, year_2, col): 

    df['diff_in_{}_{}-{}'.format(col, year_1, year_2)] = df['{}_{}'.format(col, year_1)] - df['{}_{}'.format(col, year_2)]
    return df

def change_col_names(df, year):
    '''changes column names of stats to specify the year its coming from
        returns the dataframe so needs to be caught'''
    return df.rename(columns={'Team': 'Team_{}'.format(year), 'Age': 'Age_{}'.format(year),
                              'G': 'G_{}'.format(year),'GS': 'GS_{}'.format(year), 
                              'Att': 'Att_{}'.format(year),'Yds': 'Yds_{}'.format(year), 
                              'TD': 'TD_{}'.format(year),'Lng': 'Lng_{}'.format(year), 
                              'Y/A': 'Y/A_{}'.format(year), 'Y/G': 'Y/G_{}'.format(year), 
                              'A/G': 'A/G_{}'.format(year)})

def merge_years_of_stats(df_1, df_2, year_2):
    '''df_1 already has changed column names to specify years
       df_2 will have column names changed before merged to final df'''
    df_2 = df_2.drop(['Pos', '_Tgt', '_Rec', '_Yds', '_Y/R', '_TD', '_Lng',
                      '_Y/G', 'Ctch%', 'YScm', 'RRTD', 'Fmb', 'R/G', 'Rk'], axis=1)
    df_2 = change_col_names(df_2, year_2)
    df_2['Name'] = fix_names(df_2)
    return df_1.merge(df_2, how='outer', on='Name')

df = df_2016.loc[:,['Name', 'Pos']]
df['Name'] = fix_names(df)
df['Pos'] = df['Pos'].apply(lambda x: str(x).upper())

def call_merge_stats(df, list_of_dfs, years)
	for i in range(len(list_of_dfs)):
		df = merge_years_of_stats(df, list_of_dfs[i], years[i])

def call_change_in_col(df, list_of_dfs, years, col_names):
	for i in range(len(list_of_dfs)):
		for j in range(len(col_names))
			df = change_in_col(df, list_of_dfs[i], years[i], col_names[j])

'''still need to add doc strings for each method and i need to check format'''
