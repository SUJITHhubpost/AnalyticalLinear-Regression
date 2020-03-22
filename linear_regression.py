# Linear regression implementation, Relation between 2 variables 
# Input function
# mean Function
# Correlation Function
# Regression line plot function

import math
import numpy as np
import matplotlib.pyplot as plt

import variablity as v


# input x and y

def inputs():
    x = []
    y = []
    n = int(input("Enter number of Elements: "))
    print("\n\nEnter X Values\n")
    for i in range(n):
        m = float(input("\nEnter X[{}]:".format(i)))
        x.append(m)
    print("\n\nEnter Y Values\n")
    for i in range(n):
        m = float(input("\nEnter y[{}]:".format(i)))
        y.append(m)
    return x, y

# calculate mean of x and y


def mean(x, y):
    # x, y = inputs()

    X = np.asarray(x)
    Y = np.asarray(y)

    x = np.sum(X)/len(x)
    y = np.sum(Y)/len(y)

    return x, y


# Calculate Correlation
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

# line through all y'

def Regression_line(X, Y, B, A):       
    #   Yd = bX + A 
    Yd = []

    for i in range(0,len(X)):
        Yd.append(B * X[i] + A)

    print(Yd)
    plt.scatter(X, Y)
    plt.plot(X, Yd)
    plt.scatter(X, Yd)


    
    plt.show()
    

#Line_plot
def lplot(a,b):
    plt.plot(a,b)
    plt.show()

    


if __name__ == "__main__":

    # X, Y = inputs()

    X = [1.00, 2.00, 3.00, 4.00, 5.00]
    Y = [1.00, 2.00, 1.30, 3.75, 2.25]

    Mx, My = mean(X, Y)

    sx = v.std_deviation(X)
    sy = v.std_deviation(Y)

    x, y, corr = corr(X, Y)

    r = corr


    b = r*(sy/sx)
    A = My - (b * Mx)

    print("Mx = {} ,My = {} ,sx = {}, sy = {}, r = {}\n".format(Mx, My, sx, sy, r))

    Regression_line(X, Y, b, A)




    
