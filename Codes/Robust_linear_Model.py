import matplotlib.pyplot as plt
import numpy as np
import csv
from scipy import optimize
from sklearn import linear_model




def Huber(A, X, b, y):
        if abs(y-np.dot(A,X)-b)<10:
            return (y-np.dot(A,X)-b)**2
        else:
            return 20*abs(y-np.dot(A,X)-b)-100


class nonGaussian_linear_model:
    A=None
    b=None
    X=None
    y=None
    
       
    # A constructor with choises of LossFunctions={'L1', 'L2', 'Huber'}.
    def __init__(self, LossFunction):
        self.LossFunction=LossFunction



    #A plot function to visualize the data when the input X is 1-dimensional. 
    def PlotXY(self):
        plt.scatter(self.x,self.y)
        plt.show()

    #L1LossFunction for beta=[A,b].
    def L1Loss(self, beta):
        return sum([abs(self.y[i]-np.dot(beta[:-1],self.X[i])-beta[-1]) for i in range(len(self.y))])

    #L2LossFunction for A,b.
    def L2Loss(self, beta):
        return sum([(self.y[i]-np.dot(beta[:-1],self.X[i])-beta[-1])**2 for i in range(len(self.y))])


    #HuberLossFunction
    def HuberLoss(self, beta):
        return sum([Huber(beta[:-1], self.X[i], beta[-1], self.y[i]) for i in range(len(self.y))])
    
    #Linear regression using the chosen loss function.
    def fit(self, X, y):
        self.X=X
        self.y=y

        regr=linear_model.LinearRegression()
        regr.fit(X,y)
        initial_guess=np.append(regr.coef_, regr.intercept_)

        if self.LossFunction=='L1':
            f=self.L1Loss
        if self.LossFunction=='L2':
            f=self.L2Loss
        if self.LossFunction=='Huber':
            f=self.HuberLoss
        
        beta=optimize.fmin(f, initial_guess, maxfun=10000)
        self.A=beta[:-1]
        self.b=beta[-1]
 

    def predict(self,X):
        return np.array([np.dot(self.A, X[i])+self.b for i in range(X.shape[0])])
            
            
    #Plot the residual.
    def PlotPredict(self, X, y):

        y_pred=self.Predict(X)
        
        x=np.arange(len(y))
        plt.bar(x, y, facecolor='#9999ff', label='Ground Truth')
        plt.bar(x, -y_pred, facecolor='#ff9999', label='Prediction Value')
        plt.legend()

        plt.show()    

    #Compute the R-squared
    def score(self, X, y):

        residual=np.array([y[i]-np.dot(X[i],self.A)-self.b for i in range(len(y))]);
        mean=np.mean(y)
        SSE=sum(residual**2)
        SST=sum((y-mean)**2)
        
        return 1-SSE/SST




        
        
