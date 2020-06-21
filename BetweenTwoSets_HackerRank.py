'''

hackerRank 'BetweenTwoSets'

'''
def findFactors(p):
    factors = []
    for i in range(1,p+1):
        if(p%i==0):
            factors.append(i)
    return factors
    
def getTotalX(a, b):
    # Write your code here
    fac = []
    factors = []
    
    for i in b:
        fac = findFactors(i)
        factors = factors + fac
        
    fact= []
    for j in factors:
        count = 0
        for k in a:
            if j%k ==0:
                count+=1
        if (count==len(a)):
            fact.append(j)
    
    fact_2 = set(fact)
    count_2 = 0 
    for i in fact_2:
        if(fact.count(i)==len(b)):
            count_2+=1
    
    
    print(fact)
    return count_2        

    
a = [2,4]
b = [16,32,48]
print(getTotalX(a,b))
