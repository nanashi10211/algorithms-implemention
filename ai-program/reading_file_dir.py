
# impots pandas and numpy
import numpy as np
import pandas as pd
import os

dataFileList = {}

for dirname, _, filenames in os.walk("./ai-program/.data/"):
    for filename in filenames:
        dataFileList[filename] = os.path.join(dirname, filename)
       


dataFramList = {}


for fram in dataFileList:
    dataFramList[fram] = pd.read_csv(dataFileList[fram])

for dataFram in dataFramList:
    dataFramList[dataFram].head()
    dataFramList[dataFram].info()



