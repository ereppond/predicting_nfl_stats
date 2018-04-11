import numpy as np
import scipy.stats as scs
import matplotlib.pyplot as plt
import pandas as pd
%matplotlib inline
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = 'all'
pd.set_option('display.max_columns', None)

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (precision_score,
                             recall_score,
                             confusion_matrix)
from sklearn.model_selection import train_test_split
import datetime as DT
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('basic_and_rushing_data_2015.csv')

def height_to_float(height):
    return float(float(height[0]) + float(height[2:])/12)

def get_state(place):
    '''place must be in the form of City, ST'''
    return place[-2:]

def find_nan(x):
    if str(x) == 'NaN':
        True
    else:
        return False

def remove_commas(string):
    string = string.replace(',', '')
    return float(string)

df = df.drop('Unnamed: 0', axis=1)

df['birth_date'] = pd.to_datetime(df['birth_date'])

now = pd.Timestamp(DT.datetime.now())

df['age'] = (now - df['birth_date']).apply(lambda x: round(x.days / 365.25, 2))

df['birth_state'] = df['birth_place'].apply(lambda x: get_state(str(x)))

df['height'] = df['height'].apply(lambda x: height_to_float(str(x)))

df['position_x'].value_counts()

df['birth_state'].value_counts();

df_useful = pd.read_csv('numerical_data_2015.csv')

df_useful['current_salary'].fillna('0', axis=0, inplace=True)

df_useful['current_salary'] = df_useful['current_salary'].apply(lambda x: remove_commas(str(x)))

y = df_useful['yds'].values
X = df_useful.drop(['yds'], axis=1).values

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

#df_useful = df_useful.drop('Unnamed: 0', axis=1);

#df_useful.to_csv('numerical_data_2015.csv')

df

rf = RandomForestRegressor(n_estimators=1000, max_depth=10)
rf.fit(X_train, y_train)

random_forest_grid = {'max_depth': [3, None],
                      'max_features': ['sqrt', 'log2', None],
                      'min_samples_split': [2, 4],
                      'min_samples_leaf': [1, 2, 4],
                      'bootstrap': [True, False],
                      'n_estimators': [10, 20, 40, 80],
                      'random_state': [1]}

rf_gridsearch = GridSearchCV(RandomForestRegressor(),
                             random_forest_grid,
                             n_jobs=-1,
                             verbose=True,
                             scoring='mean_squared_error')
rf_gridsearch.fit(X_train, y_train)

print("best parameters:", rf_gridsearch.best_params_)

best_rf_model = rf_gridsearch.best_estimator_

rf_score = best_rf_model.score(X_test, y_test)
rf_score

np.unique(y_test).shape

confusion_matrix(y_test, rf.predict(X_test)).shape

df = pd.read_csv('combine.csv',error_bad_lines=False)

df

df['arms'].value_counts()

