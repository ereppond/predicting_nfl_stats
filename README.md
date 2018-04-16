----
## NFL Rushing Stats
Click [here](https://www.pro-football-reference.com) to see the website where the rushing stats come from.

> This repository was made to predict NFL Rushing statistics for running backs. The predictions were made off of the differences in yards per year as well as many other differences in classic running backs' statistics each year. The age, weight, and team of each player is also accounted for in the predictive modeling. 

----
## Statistics used for each player
* Team
* Age
* The difference in total yards for each year
* Whether the player changed teams between years
* Number of games
* The difference in the total number of games started
* The difference in the total number of attempts 
* The difference in the total number of touchdowns
* The difference in the total number of longs 
* The difference in the number of yards per attempts
* The difference in the number of yards per game 
* The difference in the number of attempts per game

----
## Things to Note:

*I am using the year 2016 as the year I am testing. Once I am satisfied with the model, I will use the most recent year as a testing set *

Below are the things that should be imported for the modeling

    import pandas as pd
	import scipy.stats as scs
	import matplotlib.pyplot as plt
	import numpy as np
	from sklearn.ensemble import RandomForestClassifier
	from sklearn.metrics import (precision_score,
                             recall_score,
                             confusion_matrix)
	from sklearn.model_selection import train_test_split
	import datetime as DT
	from sklearn.linear_model import LinearRegression
	from sklearn.tree import DecisionTreeRegressor
	from sklearn.ensemble import RandomForestRegressor
	from sklearn.ensemble import GradientBoostingRegressor
	from sklearn.ensemble import AdaBoostRegressor
	from sklearn.datasets import load_boston
	from sklearn.model_selection import train_test_split, cross_val_score
	from sklearn.model_selection import GridSearchCV
	from sklearn.metrics import mean_squared_error, r2_score

	pd.set_option('display.max_columns', None)
	%matplotlib inline

[links](http://wikipedia.org)
