import pandas as pd
import numpy as np
import operator

# loading data file into the program. give the location of your csv file
ra = pd.read_excel('assignment6.xlsx', sheet_name='Sheet1')
print(dataset.head()) # prints first five tuples of your data.

# making function for calculating euclidean distance
def E_Distance(x1, x2, length):
    distance = 0
    for x in range(length):
        distance += np.square(x1[x] - x2[x])
    return np.sqrt(distance)

# making function for defining K-NN model

def knn(trainingSet, testInstance, k):
    distances = {}
    length = testInstance.shape[1]
    for x in range(len(trainingSet)):
        dist = E_Distance(testInstance, trainingSet.iloc[x], length)
        distances[x] = dist[0]
    sortdist = sorted(distances.items(), key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(sortdist[x][0])
    Count = {}  # to get most frequent class of rows
    for x in range(len(neighbors)):
        response = trainingSet.iloc[neighbors[x]][-1]
        if response in Count:
            Count[response] += 1
        else:
            Count[response] = 1
    sortcount = sorted(Count.items(), key=operator.itemgetter(1), reverse=True)
    return (sortcount[0][0], neighbors)


# making test data set
testSet = [[8.2, 2.6, 3.2, 1.8]]
test = pd.DataFrame(testSet)

for k in [3,5,7]:
    prediction, neigh = knn(dataset, test, k)
    print()
