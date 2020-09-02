#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import numpy as np
import pandas as pd

#enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))
enron_data = pickle.load(open("c:/Users/pniksirat/Downloads/ud120-projects-master/ud120-projects-master/final_project/final_project_dataset.pkl", "rb"))
print(len(enron_data))
s=pd.DataFrame(enron_data)
print(s.count)

#Finding number of POI that is true
d=s.loc['poi']
#print(d)
d2=d.where(d==1)
print(np.sum(d2))

# total stock of James Prentice
JAMESStock=s.loc['total_stock_value','PRENTICE JAMES']
#print(JAMESStock)

#email messages do we have from Wesley Colwell to POI
#print(s.loc['from_this_person_to_poi','COLWELL WESLEY'])

#value of stock options exercised by Jeffrey K Skilling
#print(s.loc['exercised_stock_options','SKILLING JEFFREY K'])

#Lay, Skilling and Fastow), who took the most $“total_payments” 
#sDollars=s.loc['total_payments','SKILLING JEFFREY K']
sDollars=s.loc['total_payments']
#Tif=sDollars.nlargest(3)
##print(sorted(sDollars[2])[-3])

sDollars=pd.DataFrame(sDollars)
df1 = sDollars.apply (pd.to_numeric, errors='coerce')
df1 = df1.dropna()
#print (df1)

#HigestDollars=(sDollars['total_payments'].head(3))
#['KENNETH LAY L', 'SKILLING JEFFREY K','FASTOW ANDREW']
DSort=df1.sort_values(by=['total_payments'],ascending=True)
#print(DSort)

###quantified salary? a known email address
EmailList=s.loc['email_address']
EmailList=pd.DataFrame(EmailList)
print(EmailList[~EmailList.isin(['NaN', 'NaT']).any(axis=1)])
#Email = EmailList.dropna()

Qsalary=pd.DataFrame(s.loc['salary'])
print(Qsalary[~Qsalary.isin(['NaN', 'NaT']).any(axis=1)])


##NaN” for their total payments
QTSalary=pd.DataFrame(s.loc['total_payments'])
QTSalary = QTSalary.apply (pd.to_numeric, errors='coerce')
print("Q Tsalary",QTSalary)
QTSalaryArray=(QTSalary.isna().sum(axis=1))
print("% NaN” for their total payments:", np.sum(QTSalaryArray)/len(QTSalaryArray))

##############%POI with NAN total payment####################
d3=d2.isna()
print("poi", np.where(d3 == True))
test1=s.loc[['poi', 'total_payments']]
test2=pd.DataFrame(test1)
#print(test2[~test2['poi'== True] & test2['total_payments'== 'NAN']])
Count=0
R=(test2.iloc[0].size)

"""
for y in range(R): 
 if (test2.iloc[0][y]==True) :
     print(test2.columns[y])
print("Tpayment\'n'")

for z in range(R):
 if  (test2.iloc[1][z]=="NaN") :
     print(test2.columns[z])
"""

for x in range(R):
    #test2.columns[test2.iloc[0]][x]
 if (test2.iloc[0][x]==True) & (test2.iloc[1][x]=="NaN") :
     print(test2.columns[x])
     Count=Count+1

##########################################################