#Program to compute the center of distribution

import math

# 1. Calculate Sum absolute deviation

def sum_ofabsolute_dev(center_of_distribution, distribution):
    sum_dev = 0
    distribution = distribution
    center_of_destribution = center_of_distribution
    for i in range(0, len(distribution)):
        sum_dev += abs(distribution[i] - center_of_destribution)
    return sum_dev


# 2.  Find minimum of absolute deviation
def minimum_of_abs(distribution):
    sum_dev = 0
    last_sum = []
    for i in range(1000):
        sum_dev = sum_ofabsolute_dev(i+1, distribution)
        last_sum.append(sum_dev)
    minVal = min(last_sum)
    ind = last_sum.index(min(last_sum))+1
    return minVal, ind

# 1. Calculate Sum squared deviation

def sum_ofsqrd_dev(center_of_distribution, distribution):
    sum_dev = 0
    distribution = distribution
    center_of_destribution = center_of_distribution
    for i in range(0, len(distribution)):
        sum_dev += (distribution[i] - center_of_destribution)**2
    return sum_dev


# 2.  Find minimum of absolute deviation
def minimum_of_absq(distribution):
    sum_dev = 0
    last_sum = []
    for i in range(1000):
        sum_dev = sum_ofsqrd_dev(i+1, distribution)
        last_sum.append(sum_dev)
    minVal = min(last_sum)
    ind = last_sum.index(min(last_sum))+1
    ind = math.sqrt(ind)
    return minVal, ind
        


if __name__ == "__main__":
    
    distribution = [2,3,4,9,16]
    distribution1 = [3, 6, 9, 10]
    minVal, index = minimum_of_abs(distribution1)
    print("Minimum Sum of absolute deviation is {} and Center of deviation is {}".format(minVal, index))
    sum_of = sum_ofsqrd_dev(index, distribution1)
    print(sum_of)
