import pandas as pd

def import_data():
    df_2011 = pd.read_csv('../data/nfl_2011_rushing_and_receiving_stats.csv')
    df_2012 = pd.read_csv('../data/nfl_2012_rushing_and_receiving_stats.csv')
    df_2013 = pd.read_csv('../data/nfl_2013_rushing_and_receiving_stats.csv')
    df_2014 = pd.read_csv('../data/nfl_2014_rushing_and_receiving_stats.csv')
    df_2015 = pd.read_csv('../data/nfl_2015_rushing_and_receiving_stats.csv')
    df_2016 = pd.read_csv('../data/nfl_2016_rushing_receiving_stats.csv')
    return df_2011, df_2012, df_2013, df_2014, df_2015, df_2016

def short_name(name):
    '''Removes unnecessary characters from ends of players names. 
    
    Args:
        name (string): name of player that need the excess characters removed
            from it.

    Returns:
        string: updated name of player.

    ''' 
    for i in range(len(name)):
        if name[i] in "*+\\":
            return name[:i]

def fix_names(df):
    '''Calls short_name to fix the extra characters in each name. 
    
    Args:
        df (pandas DataFrame): DataFrame that you need to change the names of.

    Returns:
        pandas DataFrame: updated DataFrame with fixed names of players.

    '''
    return df['Name'].apply(lambda x: short_name(x))

def change_in_teams(df, year_1, year_2): 
    '''Adds column for whether player changed teams from one year to another. 
    
    Args:
        df_1 (pandas DataFrame): DataFrame that you would like to merge onto.
        df_2 (pandas DataFrame): DataFrame that you would like to merge 
            to df_1.
        year_2 (string): string of the year that refers to the year that df_2 
            comes from.

    Returns:
        pandas DataFrame: df with added column for the change in teams for 
            those years.

    '''
    new_col_name = 'diff_in_team_{}-{}'.format(year_1, year_2)
    team_1 = 'Team_{}'.format(year_1)
    team_2 = 'Team_{}'.format(year_2)
    df[new_col_name] = df[team_1] != df[team_2]
    return df


def change_in_col(df, year_1, year_2, col):
    '''Calculates the difference for a column from one year to another. 

    Args:
        df (pandas DataFrame): DataFrame that you would like to merge onto.
        year_1 (string): string of the year that refers to the year that
            will have year 2 subtracted from it.
        year_2 (string): string of the year that refers to the year that 
            needs to be subtracted from year 2.

    Returns:
        pandas DataFrame: dataframe with added column for the difference in
            the columns for those years for each player.

    '''
    new_col_name = 'diff_in_{}_{}-{}'.format(col, year_1, year_2)
    col_name_1 = '{}_{}'.format(col, year_1)
    col_name_2 = '{}_{}'.format(col, year_2)
    df[new_col_name] = df[col_name_1] - df[col_name_2]
    return df


def change_col_names(df_2, year):
    '''Changes column names of stats to specify the year its coming from. 

    Args:
        df (pandas DataFrame): DataFrame that you would like to fix the column
            names of.
        year (string): string of the year that refers to the year that df 
            comes from.

    Returns:
        pandas DataFrame: cleaned dataframe with correct columns names of df.

    '''
    df_2 = df_2.rename(columns={'Team': 'Team_{}'.format(year),
                            'Age': 'Age_{}'.format(year),
                            'G': 'G_{}'.format(year),
                            'GS': 'GS_{}'.format(year),
                            'Att': 'Att_{}'.format(year),
                            'Yds': 'Yds_{}'.format(year),
                            'TD': 'TD_{}'.format(year),
                            'Lng': 'Lng_{}'.format(year),
                            'Y/A': 'Y/A_{}'.format(year),
                            'Y/G': 'Y/G_{}'.format(year),
                            'A/G': 'A/G_{}'.format(year)})
    return df_2


def merge_years_of_stats(df_1, df_2, year_2):
    '''This method cleans df_2 to prepare it to be merged with df_1. Then it
       merges with df_1.  

    Args:
        df_1 (pandas DataFrame): DataFrame that you would like to merge onto.
        df_2 (pandas DataFrame): DataFrame that you would like to merge to df_1.
        year_2 (string): string of the year that refers to the year that df_2 
            comes from.

    Returns:
        pandas DataFrame: merged dataframe with correct columns names for the 
            new data added to df_1.

        Catching the return is necessary- needs to be caught by what will be
            the final df
    '''
    df_2 = df_2.drop(['Pos', '_Tgt', '_Rec', '_Yds', '_Y/R', '_TD', '_Lng',
                      '_Y/G', 'Ctch%', 'YScm', 'RRTD', 'Fmb', 'R/G', 'Rk'], 
                      axis=1)
    df_2['Name'] = fix_names(df_2)
    df_2 = change_col_names(df_2, year_2)
    return df_1.merge(df_2, how='outer', on='Name')


if __name__ == '__main__':
    df_2011, df_2012, df_2013, df_2014, df_2015, df_2016 = import_data()
    list_of_dfs = [df_2011, df_2012, df_2013, df_2014, df_2015, df_2016]
    list_of_years = ['2011', '2012', '2013', '2014', '2015', '2016']
    col_names = ['Yds', 'GS', 'TD', 'Lng', 'Y/A', 'Y/G', 'A/G']
    df = df_2016.loc[:,['Name', 'Pos']]
    df['Name'] = fix_names(df)
    df['Pos'] = df['Pos'].apply(lambda x: str(x).upper())
    for i in range(len(list_of_dfs)):
        df = merge_years_of_stats(df, list_of_dfs[i], list_of_years[i])
    list_of_years = ['2011', '2012', '2013', '2014', '2015']
    for i in range(len(list_of_years) - 1):
        for j in range(len(col_names)):
            df = change_in_col(df, list_of_years[i], list_of_years[i + 1], 
                col_names[j])
    df.to_csv('../data/data_with_differences.csv')
