def designerPdfViewer(h, word):
   
    alphabet_list = []
    for i in range(ord('a'),ord('z')+1):
        alphabet_list.append(i)
    
    p = []
    p = dict(zip(alphabet_list,h))
    

    n = []
    for t in word:
        l = ord(t)
        r = p[l]
        n.append(r)
    
    print(max(n)*len(word))
    
h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,7]
word = 'zaba'

designerPdfViewer(h,word)
