def factorial(a):
    product = 1
    while(a>0):
        product*=a
        a-=1
    return product  
    
    
print(factorial(6))
