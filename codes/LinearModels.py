import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import ExtraTreesRegressor
import math
from Robust_Regression import nonGaussian_linear_model
import operator



#Load data
data = np.genfromtxt('/Users/yajingleo/Downloads/data/China_Air_Pollution/Beijing_PM_data_3/Beijing_PM_9_17.csv',delimiter=',')
"""
#Get rid of the invalid data where the null value appears.
bad_indices=[]
for i in range(data.shape[0]):
    if data[i,0]==0 or data[i,1]==0 or data[i,0]>=data[i,1]: 
        bad_indices.append(i)
        
data=np.delete(data, bad_indices, 0)
"""
m=data.shape[0]

print ("The size of the data is %i" % m)

#Split the data into training set and test set
X_train=data[1:-30,1:-1]
X_test=data[-30:,1:-1]

#Split the target into training set and test set
y_train=data[1:-30, 0]
y_test=data[-30:,0]


#Create linear regression objects
Estimators={
"Odinary Least Squares":linear_model.LinearRegression(normalize=True),

"Ridge CV":linear_model.RidgeCV(alphas=[10000, 1000, 100, 10, 1, 0.1, 0.01, 0.001, 0.0001, 0.00001]),

"LASSO CV":linear_model.LassoCV(alphas=[10000, 1000, 100, 10, 1, .1, .01, .001, .0001,0.000001]),

"ExtraTree Regression":ExtraTreesRegressor(n_estimators=10, max_features='auto', random_state=0),

"Random Forest Regression":RandomForestRegressor(),

"M-Regression": nonGaussian_linear_model('Huber'),

"Absolute Loss Regression": nonGaussian_linear_model('L1')
}

colors=['#808000','black', 'red', 'green', 'purple', 'orange', 'pink']
axis_font = {'fontname':'Arial', 'size':'20'}

TrainError={}
TestError={}
VarianceScore={}

#Fit data into models.
i=0
for name, regr in Estimators.items():
    regr.fit(X_train, y_train)
    y_pred=regr.predict(X_test)
    x=np.linspace(1, 30, 30)
    plt.plot(x, y_pred, color=colors[i],  label=name)
    
    TestError[name]=math.sqrt(np.mean((y_pred-y_test)**2))/math.sqrt(np.mean(y_test**2))
    TrainError[name]=math.sqrt(np.mean((y_train-regr.predict(X_train))**2))/math.sqrt(np.mean(y_train**2))
    VarianceScore[name]=regr.score(X_train, y_train)
    i+=1

plt.plot(x, y_test, color='blue', linewidth=2, label='True Value')
 
plt.title("PM2.5 Values Prediction in Beijing at 17PM based on data at 9Am", **axis_font)
plt.xlabel("Dates", **axis_font)
plt.xticks(np.arange(min(x), max(x)+1, 1))
plt.legend(loc='upper left')


plt.show()

#Plot the prediction results.
fig = plt.figure()
width=.35
plt.subplot(211)
plt.bar(np.arange(7), TrainError.values(), color='#007FFF', width=width)
plt.xticks(np.arange(7)+ width / 2, TrainError.keys())
fig.autofmt_xdate()
plt.ylim(0, 1)
plt.title("Training Errors", **axis_font)


plt.subplot(212)
width=.35
A=sorted(TestError.items(), key=operator.itemgetter(1))
TestErrorValues=np.array([A[i][1] for i in range(7)])
TestErrorKeys=[A[i][0] for i in range(7)]
plt.bar(np.arange(7), TestError.values(), color='#007FFF', width=width)
plt.xticks(np.arange(7)+ width / 2, TestError.keys())
fig.autofmt_xdate()
plt.ylim(0, 1)
plt.title("Test Errors", **axis_font)
plt.show()


fig = plt.figure()
width=.35
A=sorted(VarianceScore.items(), key=operator.itemgetter(1))
VarianceScoreValues=np.array([A[i][1] for i in range(7)])
VarianceScoreKeys=[A[i][0] for i in range(7)]
plt.bar(np.arange(7), VarianceScoreValues, color='#007FFF', width=width)
plt.xticks(np.arange(7)+ width / 2, VarianceScoreKeys)
fig.autofmt_xdate()
plt.ylim(0, 1)
plt.title("R^2 Scores", **axis_font)
plt.show()


