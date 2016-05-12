import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
import math

#Load data
data = np.genfromtxt('/Users/yajingleo/Downloads/data/China_Air_Pollution/Beijing.csv',delimiter=',')

m=data.shape[0]

#Split the data into training set and test set
X_train=data[1:-30,1:10]
X_test=data[-30:,1:10]

#Split the target into training set and test set
y_train=data[1:-30, 0].reshape(m-31,1)
y_test=data[-30:,0].reshape(30,1)

#Create linear regression object
regr=linear_model.LinearRegression()

#Train the model
regr.fit(X_train, y_train)

#Predict the test set
y_pred=regr.predict(X_test)

#The coefficients
print(regr.coef_, regr.intercept_)

#The mean of test set
print("The mean PM2.5 of the test set is: %.2f" % np.mean(y_test))

#The mean standard error
relative_error=np.array([1-(y_pred[i]/y_test[i]) for i in range(30) if y_test[i]!=0])
print("The standard error is:  %.2f" % math.sqrt(np.mean(relative_error**2)))

#The variance score
print("The variance score is: %2f" % regr.score(X_test, y_test))

#X-axis
x=np.linspace(1, 30, 30)


#Plot the regression on the test set
plt.bar(x, y_test, color='b', label="Real value")
plt.bar(x, -y_pred, color='r', label="Predicted value")
plt.legend()

plt.show()
