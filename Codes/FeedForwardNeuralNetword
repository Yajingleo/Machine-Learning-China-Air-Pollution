import numpy as np
import random



class Network:
  
  def __init__(self,size):
    self.num_layers = len(size)
    self.size = size
    self.bias = [np.random.randn(y,1) for y in size[1:]]
    self.weights = [np.random.randn(y,x) for x,y in zip(size[:-1],size[1:])]
    
    
  def feedforward(self, a):
    for b, w in zip(self.bias,self.weights):
      a = sigmoid(np.dot(w,a) + b)
    return a
    
  ##Stochastic Gradient Descent  
  def SGD(self, training_data, epochs, mini_batch_size, eta, test_data = None):
    if test_data:
      n_test = len(test_data)
    n = len(training_data)
    for j in range(epochs):
      random.shuffle(training_data)
      mini_batchs = [training_data[k:k+mini_batch_size] for k in range(0, n , mini_batch_size)]
      for batch in mini_batchs:
        self.update_mini_batch(batch,eta)
      if test_data:
        print 'Epoch {0}: {1} / {2}'.format(j,self.evaluate(test_data),n_test)
      else:
        print 'Epoch {0} complete'.format(j)
        
  def update_mini_batch(self,batch,eta):
    nabla_b = [np.zeros(b.shape) for b in self.bias]
    nabla_w = [np.zeros(w.shape) for w in self.weights]
    for x,y in batch:
      delta_nabla_b, delta_nabla_w = self.backprop(x,y)
      nabla_b = [nb + dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]
      nabla_w = [nw + dnw for nw, dnw in zip(nabla_w, delta_nabla_w)]
    self.weights = [w - (eta/len(batch))*nw for w,nw in zip(self.weights, nabla_w)]
    self.bias = [b - (eta/len(batch))*nb for b, nb in zip(self.bias, nabla_b)]
   
  
  def backprop(self,x,y):
    nabla_b = [np.zeros(b.shape) for b in self.bias]
    nabla_w = [np.zeros(w.shape) for w in self.weights]
    activation = x
    activations = [x]
    zs = []
    
    for b,w in zip(self.bias,self.weights):
      z = np.dot(w, activation) + b
      zs.append(z)
      activation  = sigmoid(z)
      activations.append(activation)
    delta = self.cost_derivative(activations[-1],y)*sigmoid_prime(zs[-1]) 
    nabla_b[-1] = delta
    nabla_w[-1] = np.dot(delta, activations[-2].transpose())
    
    for l in range(2, self.num_layers):
      z = zs[-l]
      sp = sigmoid_prime(z)
      delta = np.dot(self.weights[-l+1].transpose(),delta) * sp
      nabla_b[-l] = delta
      nabla_w[-l] = np.dot(delta, activations[-1-l].transpose())
    
    return (nabla_b,nabla_w)
  
  
   
  def evaluate(self, test_data):
    test_results = [(np.argmax(self.feedforward(x)),y) for (x,y) in test_data] 
    return sum([int(x==y) for (x,y) in test_results])
   
  def cost_derivative(self, output_activations, y):
    return (output_activations - y)
    
    
    
def sigmoid(z):
  return 1.0/(1.0 + np.exp(-z))
    
def sigmoid_prime(z):
  return sigmoid(z)*(1-sigmoid(z))
  
  
