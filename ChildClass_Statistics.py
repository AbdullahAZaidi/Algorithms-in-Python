'''
Stats Class : Mean, Standard Deviation, Variance

'''
import math as math
class Statistics :
    
    def __init__(self, arr):
        self.arr = arr
        
        
    def calculateMean(self):
        sum_m = 0
        for i in self.arr:
            sum_m +=i 
        
        return (sum_m/len(self.arr))
        
    
    def calculateSD(self):
        sum_d = 0
        mean = self.calculateMean()
        for i in self.arr:
            sum_d += (i-mean)**2
            
        return (math.sqrt (sum_d/(len(self.arr))))
        
    
    def calculateVariance(self):
        SD = self.calculateSD()
        return SD**2
        

class Standard(Statistics):
    
    def __init__(self,b):
        super().__init__(a)
        
    def calculateMean(self):
        sum_m = 0
        for i in self.arr:
            sum_m +=i 
        
        return (sum_m*2/len(self.arr))
        
            
a = [9, 2, 5, 4, 12, 7, 8, 11, 9, 3, 7, 4, 12, 5, 4, 10, 9, 6, 9, 4] 
x = Statistics(a)
y = Standard(a)
print (x.calculateMean(),x.calculateSD(),x.calculateVariance(),y.calculateMean())
