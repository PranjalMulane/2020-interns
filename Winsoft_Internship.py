
#WINSOFT INTERNSHIP TASK
##########################################################################3
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

#-------------------TASK-1---------------------------

inr = (df.loc[:'INR'])

inrval = (list(inr))

plt.plot(datelist[:30], inrval[:30])    

plt.xlabel('Dates')

plt.ylabel('EUR to INR')

plt.title('Graph of INR exchange rate against EUR') 

plt.show()

#--------------------TASK - 2------------------------

inr = (df.loc[:'INR','GBP'])

inrval = (list(inr))

plt.plot(datelist[:30], inrval[:30])    

plt.xlabel('Dates')

plt.ylabel('EUR to INR and GBP')

plt.title('Graph of INR and GBP exchange rate against EUR') 

plt.show()


#--------------------TASK 3----------------------------


newDataFile = open('latest-rates.json')

newData = json.load(newDataFile)

newRates = (data['rates'])

newOd = collections.OrderedDict(sorted(newRates.items()))

newDatelist = list(newOd.keys())

newVal = list(newRates.values())

newDf = pd.DataFrame(newVal, index = newDatelist)

newInr = (newDf.loc[:'INR','GBP'])

newInrval = (list(newInr))



inr = (df.loc[:'INR','GBP'])
inrval = (list(inr))

plt.plot(newDatelist[:30], newInrval[:30], label = 'latest rates') 

plt.plot(datelist[:30], inrval[:30], label = 'Jan 2019')   

plt.xlabel('Dates')

plt.ylabel('EUR to INR and GBP')

plt.title('Graph of INR and GBP exchange rate against EUR') 

plt.show()






















