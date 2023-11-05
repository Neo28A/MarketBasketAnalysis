# -*- coding: utf-8 -*-
"""MarketBasketAnalysisUsingAPRIOR.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Pf7MHmmgYNIGeMB0bHKkpbOR8CogTPfC
"""

# @title Importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# @title Uploading Dataset
from google.colab import files
uploaded = files.upload()

# @title Importing Dataset
dataset = pd.read_csv('dataset.csv')
print(dataset.shape)
print(dataset.head(5))

# @title Data Pre-Processing
transactions = []
for i in range(0, 7500):
  transactions.append([str(dataset.values[i,j]) for j in range(0,20)])

# @title converting into numpy array
transactions = np.array(transactions)

transactions

# @title frequency of most popular items
color = plt.cm.rainbow(np.linspace(0, 1, 40))
dataset[0].value_counts().head(50).plot.bar(color = color, figsize=(13,5))
plt.title('Frequency of most popular 50 items', fontsize = 20)
plt.xticks(rotation = 90 )
plt.grid()
plt.show()

# @title Training APRIORI
!pip install apyori
from apyori import apriori
rules = apriori(transactions = transactions, min_support = 0.003, min_confidence = 0.2, min_lift = 3, min_length = 2)

results = list(rules)
results

# @title Results in DataFrame
lhs         = [tuple(result[2][0][0])[0] for result in results]
rhs         = [tuple(result[2][0][1])[0] for result in results]
supports    = [result[1] for result in results]
confidences = [result[2][0][2] for result in results]
lifts       = [result[2][0][3] for result in results]
resultsinDataFrame = pd.DataFrame(zip(lhs, rhs, supports, confidences, lifts), columns = ['Left Hand Side', 'Right Hand Side', 'Support', 'Confidence', 'Lift'])
resultsinDataFrame