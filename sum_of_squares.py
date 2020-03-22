# Compute the sum of squares Y
# Convert raw scores to deviation scores
# Compute predicted scores from a regression equation
# Partition sum of squares Y into sum of squares predicted and sum of squares error
# Define r2 in terms of sum of squares explained and sum of squares Y

import math
import variablity as v
import numpy as np
import reg_functions as r

# Squared difference of Y from Mean.
def SSY(array):
    mean2 = np.sum(array)
    mean = mean2/len(array)
    ssy, sq_diff = 0, 0

    for y in array:
        sq_diff = (y - mean)**2
        ssy = ssy + sq_diff
    return ssy

def main():
    X = [1.00, 2.00, 3.00, 4.00, 5.00]
    Y = [1.00, 2.00, 1.30, 3.75, 2.25]
    
    print("X: {}\n".format(X))
    print("y: {}\n".format(Y))
    
    # SSX is the sum of the squared deviations of X from the mean
    SSX = r.y2(X)
    
    print("Sum of the squared deviations of X from the mean or SSX : {}\n".format(SSX))    
    
    # SSY is the sum of the squared deviations of Y from the mean
    SSY = r.y2(Y)
    
    print("Sum of the squared deviations of Y from the mean or SSY : {}\n".format(SSY))
    
    Yd = r.y_dash(X, Y)
    
    print("Predicted value Y' : {}\n".format(Yd))
    
    # the sum of squares predicted (SSY') 
    SSY_d = r.y2(Yd)
    
    
    print("The sum of squares deviations of Y from the mean predicted or SSY' : {}\n".format(SSY_d))
    
    # The sum of squares error is the sum of the squared errors of prediction.
    SSE = r.y_yd2(Y, Yd)
        
    print("sum of squares error Y-Y' or SSE : {}\n".format(SSE))
    
    
    if round(SSY, 3) == round(SSE + SSY_d, 3):
        print("Standard Error : {}\n".format(r.stderr(X, Y)))
    

if __name__ == '__main__':
    main()
    