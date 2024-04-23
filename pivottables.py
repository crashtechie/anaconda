import numpy as np
import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
age = pd.cut(titanic['age'], [0, 18, 80])
fare = pd.qcut(titanic['fare'], 2)
#print(titanic.head())
#print(titanic.groupby('sex')[['survived']].mean())
#print(titanic.groupby(['sex','class'])['survived'].aggregate('mean').unstack())
#print(titanic.pivot_table('survived', index='sex', columns='class'))
print(titanic.pivot_table('survived', ['sex', age], [fare, 'class']))
