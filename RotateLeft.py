def LeftRotate(a,d):
    b = []
    n = len(a)
    for i in range(d):
        
        a.append(a[0])
        a.pop(0)
        
    return a


a = [1,2,3,4,5]
print(LeftRotate (a,2))
