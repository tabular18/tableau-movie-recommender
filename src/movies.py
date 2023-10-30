import pandas as pd
import numpy as np
import nltk
import re
import string
movielist=pd.read_csv('./Data/ml-latest-small/tags.csv')

print(len(movielist))
print(movielist.head())
print(movielist.info())