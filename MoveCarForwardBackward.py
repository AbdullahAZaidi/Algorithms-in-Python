Move Car Forward on 'A' and double the speed on every instance. 
On 'R' set the speed to 1.
Move the Car Backward for A's that follows the 'R' with double the speed for every instance.

'''


def FindPosition (a):
    speed = 1
    position = 0
    count = 0
    for i in a:
        if (i == 'A'):
            position+=speed
            speed*=2
            count+=1
        
        
        elif (i == 'R'):
            speed = 1
            count+=1
            break
            # elif (i == 'A' and i-1 == "R"):
            # speed*= -2
            # position+=speed
            
    for i in range(count+1, len(a)):
        if (a[i] == 'A'):
            position-=speed
            speed*=2
            
            
        elif (a[i] == 'R'):
            speed = 1
        
    return position
    

print(FindPosition ('RAAAA'))
