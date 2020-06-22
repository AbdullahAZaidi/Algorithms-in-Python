def RotateRight(a,d):
    b = []
    n = len(a)
    for i in range(d):
        
        a.insert(0,a[n-1])
        a.pop()
        
    return a


a = [1,2,3,4,5]
print(LeftRotate (a,2))
