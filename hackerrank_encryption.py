def encryption(s):
    a = s.replace(" ","")
    count = len(a)
    value = math.sqrt(count)
    low_value = math.floor(value)
    high_value = math.ceil(value)
    
    print (low_value, high_value)
    
    z = count%(high_value**2)
    
    for i in range(z):
        a = a+'?'
        
    print (a)

    b = []
    c = []
    d = ""

    for i in range(high_value):
        b.append([])
        for k in range(high_value):
            b[i].append(a[k+i*high_value])
            
    
    for i in range(high_value):
        c.append([])
        for k in range(high_value):
            c[i].append(b[k][i])
            
            
    for i in range(high_value):
        for k in (c[i]):
            d+=k
        d+=" "
         
        
    d = d.replace("?","")
            
    return (d)
