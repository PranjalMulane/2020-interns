

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




























'''
import pandas as pd
import json
data = json.load(open('data.json'))


data=rates.sort_values()
df = pd.read_json('data.json')
df.head()
#print(data)

print(type(data))



'''