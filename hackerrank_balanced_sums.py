def balancedSums(arr):
    for i in range(len(arr)):
        if (i==0):
            sum_left = 0
            sum_right = sum(arr[1:len(arr)])
        else:
            sum_left = sum(arr[0:i])
            sum_right = sum(arr[i+1:len(arr)])
            
        print (sum_left, sum_right)
            
        if (sum_left==sum_right):
            return ('YES')
        break 
        else:
            return ('NO')                
      


        
balancedSums([1, 2, 3, 3])
