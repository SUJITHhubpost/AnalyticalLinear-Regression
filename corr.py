#Program to find correlation between X and Y 

import math
import numpy as np
import variablity

#input x and y

def inputs():
    x = []
    y = []
    n =int(input("Enter number of Elements: "))
    print("\n\nEnter X Values\n")
    for i in range(n):
        m = int(input("\nEnter X[{}]:".format(i)))
        x.append(m)
    print("\n\nEnter Y Values\n")
    for i in range(n):
        m = int(input("\nEnter y[{}]:".format(i)))
        y.append(m)
    return x,y

#calculate mean of x and y
def mean(x, y):
    # x, y = inputs()

    X = np.asarray(x)
    Y = np.asarray(y)

    x = int(np.sum(X)/len(x))
    y = int(np.sum(Y)/len(y))

    return x, y

    


def corr(X, Y):
    x = 0
    y = 0

    X = np.asarray(X)              # X = [1, 3, 3, 1 ]
    Y = np.asarray(Y)              # Y = [2, 4, 4, 2]

    x, y = mean(X, Y)              # x = 2, y = 3
    x = np.full((1, len(X)), x)    # x = [2, 2, 2, 2]
    y = np.full((1, len(Y)), y)    # y = [3, 3, 3, 3]

    x = X - x
    y = Y - y

    x2 = x ** 2
    y2 = y ** 2
    xy = x * y

    div1 = np.sum(xy)
    a = np.sum(x2) * np.sum(y2)
    b = math.sqrt(a)
    corr = div1 / b

    return x, y, corr


if __name__ == "__main__":
    
    X, Y = inputs()  

    x ,y ,corr = corr(X, Y)
    print("X = {}\nY = {}\nx = {}\ny = {}\nCorrelation = {}\n".format(X, Y, x ,y ,corr))
    
  
    
