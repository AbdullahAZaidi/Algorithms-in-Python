def binary_search(input_array, value):
    """Your code goes here."""
    n = len(input_array)
    first = 0; last = n-1; 
    for i in range(first, last):
         middle = int((first + last)/2);
         if (input_array[middle] > value):
             last = middle; 
         elif (input_array[middle] == value):
             return middle
             break;
         elif (first == last-1):
             return -1
             break;
         else :
             first = middle;


    
   

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print (binary_search(test_list, test_val1))
print (binary_search(test_list, test_val2))
