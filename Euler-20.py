def sunfact(a):
    res = 1
    for i in range(1,a+1):
        res = res * i
    return sum([int(i) for i in list(str(res))])
    
print(sunfact(100))    
    
