

import json 
import collections
import pandas as pd
import matplotlib.pyplot as plt
import requests

DataFile = open('data.json')

data = json.load(DataFile)

rates = (data['rates'])

od = collections.OrderedDict(sorted(rates.items()))

datelist = list(od.keys())

val = list(rates.values())

df = pd.DataFrame(val, index = datelist)

inr = (df.loc[:'INR'])

inrval = (list(inr))


plt.plot(datelist[:30], inrval[:30])    

plt.xlabel('Dates')

plt.ylabel('EUR to INR')

plt.show()



























