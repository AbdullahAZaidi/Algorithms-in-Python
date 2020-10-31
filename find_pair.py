def findpair(n, ar):
    ar_s = set(ar)
    count = 0
    pair = 0

    for i in ar_s:
        for k in ar:
            if (i==k):
                count+=1
        pair+= count//2
        count = 0
    
    return pair
