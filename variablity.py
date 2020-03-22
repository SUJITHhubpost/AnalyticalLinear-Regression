#Functions to  calculate variabilty, Varience and standard deviation

import math
#Find the variance of a distribution

def variance(distribution):
    median = (max(distribution) + min(distribution))/2
    diff_sq = 0
    diff = 0
    variance = 0
    for i in range(0, len(distribution)):
        diff = distribution[i] - median
        diff_sq = diff ** 2
        print("{} {}".format(diff_sq,len(distribution)))
        variance += diff_sq
        # print(variance)
    
    return variance/len(distribution)


#Find the Standard deviation of a distribution

def std_deviation(distribution):
    return math.sqrt(variance(distribution))
    

if __name__ == "__main__":
    dist = [9,9,9,8,8,8,8,7,7,7,7,7,6,6,6,6,6,6,5,5]
    dist2 = [4,4,5,5,5,5,6,6,6,7,7,7,8,8,9,9,9,10,10,10]
    dist3 = [11, 8, 7, 12, 13, 13, 13, 13]
    print("Variance: {}\nStandard Deviation: {}".format(variance(dist3),std_deviation(dist3)))
    print()

