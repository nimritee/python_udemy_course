import numpy as np
from sklearn.metrics import mean_absolute_error as mae
from sklearn.metrics import mean_squared_error
import math


array1 = np.array([3.88,4.55,5.22,5.88,6.56,7.22,7.89,8.56])
array2 = np.array([5.72,6.37,7.01,7.66,8.30,8.95,9.60,10.25])

difference_array = np.subtract(array1, array2)
squared_array = np.square(difference_array)
mse = squared_array.mean()

print(mse)

actual = [3.88,4.55,5.22,5.88,6.56,7.22,7.89,8.56]
pred = [5.72,6.37,7.01,7.66,8.30,8.95,9.60,10.25]

#calculate MAE
print(mae(actual, pred))


y_actual = [3.88,4.55,5.22,5.88,6.56,7.22,7.89,8.56]
y_predicted = [5.72,6.37,7.01,7.66,8.30,8.95,9.60,10.25]
 
MSE = mean_squared_error(y_actual, y_predicted)
 
RMSE = math.sqrt(MSE)
print("Root Mean Square Error:\n")
print(RMSE)
