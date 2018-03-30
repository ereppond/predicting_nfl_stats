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

combine = pd.read_csv('~/galvanize/Data/nfl/combine.csv',error_bad_lines=False)

'''1999'''
combine_1999 = combine[['name', 'weight', 'year', 'fortyyd', 'twentyss', 
                       'threecone', 'vertical', 'broad', 'bench']]

combine_1999 = combine_1999[combine_1999['year'] == 1999]
'''2000'''
combine_2000 = combine[['name', 'weight', 'year', 'fortyyd', 'twentyss', 
                       'threecone', 'vertical', 'broad', 'bench']]

combine_2000 = combine_2000[combine_2000['year'] == 2000]
'''2001'''
combine_2001 = combine[['name', 'weight', 'year', 'fortyyd', 'twentyss', 
                       'threecone', 'vertical', 'broad', 'bench']]

combine_2001 = combine_2001[combine_2001['year'] == 2001]
'''2002'''
combine_2002 = combine[['name', 'weight', 'year', 'fortyyd', 'twentyss', 
                       'threecone', 'vertical', 'broad', 'bench']]

combine_2002 = combine_2002[combine_2002['year'] == 2002]
'''2003'''
combine_2003 = combine[['name', 'weight', 'year', 'fortyyd', 'twentyss', 
                       'threecone', 'vertical', 'broad', 'bench']]

combine_2003 = combine_2003[combine_2003['year'] == 2003]
'''2004'''
combine_2004 = combine[['name', 'weight', 'year', 'fortyyd', 'twentyss', 
                       'threecone', 'vertical', 'broad', 'bench']]

combine_2004 = combine_2004[combine_2004['year'] == 2004]
'''2005'''
combine_2005 = combine[['name', 'weight', 'year', 'fortyyd', 'twentyss', 
                       'threecone', 'vertical', 'broad', 'bench']]

combine_2005 = combine_2005[combine_2005['year'] == 2005]
'''2006'''
combine_2006 = combine[['name', 'weight', 'year', 'fortyyd', 'twentyss', 
                       'threecone', 'vertical', 'broad', 'bench']]

combine_2006 = combine_2006[combine_2006['year'] == 2006]
'''2007'''
combine_2007 = combine[['name', 'weight', 'year', 'fortyyd', 'twentyss', 
                       'threecone', 'vertical', 'broad', 'bench']]

combine_2007 = combine_2007[combine_2007['year'] == 2007]
'''2008'''
combine_2008 = combine[['name', 'weight', 'year', 'fortyyd', 'twentyss', 
                       'threecone', 'vertical', 'broad', 'bench']]

combine_2008 = combine_2008[combine_2008['year'] == 2008]
'''2009'''
combine_2009 = combine[['name', 'weight', 'year', 'fortyyd', 'twentyss', 
                       'threecone', 'vertical', 'broad', 'bench']]

combine_2009 = combine_2009[combine_2009['year'] == 2009]
'''2010'''
combine_2010 = combine[['name', 'weight', 'year', 'fortyyd', 'twentyss', 
                       'threecone', 'vertical', 'broad', 'bench']]

combine_2010 = combine_2010[combine_2010['year'] == 2010]
'''2011'''
combine_2011 = combine[['name', 'weight', 'year', 'fortyyd', 'twentyss', 
                       'threecone', 'vertical', 'broad', 'bench']]

combine_2011 = combine_2011[combine_2011['year'] == 2011]
'''2012'''
combine_2012 = combine[['name', 'weight', 'year', 'fortyyd', 'twentyss', 
                       'threecone', 'vertical', 'broad', 'bench']]

combine_2012 = combine_2012[combine_2012['year'] == 2012]
'''2013'''
combine_2013 = combine[['name', 'weight', 'year', 'fortyyd', 'twentyss', 
                       'threecone', 'vertical', 'broad', 'bench']]

combine_2013 = combine_2013[combine_2013['year'] == 2013]
'''2014'''
combine_2014 = combine[['name', 'weight', 'year', 'fortyyd', 'twentyss', 
                       'threecone', 'vertical', 'broad', 'bench']]

combine_2014 = combine_2014[combine_2014['year'] == 2014]
'''2015'''
combine_2015 = combine[['name', 'weight', 'year', 'fortyyd', 'twentyss', 
                       'threecone', 'vertical', 'broad', 'bench']]

combine_2015 = combine_2015[combine_2015['year'] == 2015]