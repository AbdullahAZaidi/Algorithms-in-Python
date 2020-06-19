import math

#reverseArray function below.

def reverseArray(a):
    n = len(a)
    half = n/2
    for i in range(int(half)):
        temp = a[i]
        a[i] = a[n-i-1]
        a[n-i-1] = temp

    return a
