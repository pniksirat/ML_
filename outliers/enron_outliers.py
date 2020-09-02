#!/usr/bin/python

import pickle
import sys
import os
import matplotlib.pyplot
#sys.path.append("../tools/")
#os.chdir(os.path.join(os.path.abspath(os.curdir),"tools\\"))
from feature_format import featureFormat, targetFeatureSplit
#os.chdir('..')


### read in data dictionary, convert to numpy array
#data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "rb") )
data_dict = pickle.load(open(os.path.join(os.path.abspath(os.curdir),"final_project\\final_project_dataset.pkl"), "rb") )
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


### your code below

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()


