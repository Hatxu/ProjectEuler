def fibbonaci(w):
    a = 0
    b = 1
    c = 1
    x=[]
    while len(str(a)) != w:
        c=a
        a=b
        b = b+c
        x.append(a)   
    return a,x.index(a)+1
    
print(fibbonaci(1000))    
