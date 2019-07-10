def loop(d):
    a = []
    b = []
    x = 1
    R = False
    while R == False:
        if x==0:
            return 0
        x=x*10
        if x%d not in b:
            a.append(int(x/d))
            x=x%d
            b.append(x)
        else:
            a.append(int(x/d))
            R= True
    return len(a)
        
def prob26(a):
    z = 0
    x = []
    for i in range(1,a+1):
        z = loop(i)
        x.append((z,i))
    return sorted(x)
    
print(prob26(1000)[-1])
