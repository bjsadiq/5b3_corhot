#Create functions to calculate the following statistical measures:
# 1. Mean
# 2. Median
# 3. Variance
# 4. Standard Deviation
# 5. Skewness

list = []
n = int(input("Enter the number of elements: "))
for x in range(0,n):
    number = int(input(":>"))
    list.append(number)

# Mean

def mean_x (x):
    mean_x = sum(x)/len(x)
    return round (mean_x,2)

print(f"The mean is {mean_x(list)}")

# Median

def median (x):
    list_2 = list.sort()
    if n%2 != 0:
        median = int (((n+1)/2)-1)
        return list[median]
    else:
        median1 = int((n/2)-1)
        median2 = int(n/2)

    return (list[median1] + list[median2])/2
print(f"The median is {median(list)}")

# Variance

def variance (x):
    variance = sum((i - mean_x(list)**2 for i in list)/ len(list) - 1)
    return round (variance,4)
print(f"The variance is {variance(list)}")

#Standard Deviation

def std_dev (x):
    std_dev = (variance(list))**0.5
    return round (std_dev,4)
print(f"The standard deviation is {std_dev(list)}")

#Skewness

def skewness ():
    skewness = 3*(mean_x(list - median(list))/std_dev(list))
    return skewness
print(f"The skewness is {skewness()}")
