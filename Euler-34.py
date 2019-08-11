def factsum(valor):
    numdcit= {'0':1,'1':1,'2':2,'3':6,'4':24,'5':120,'6':720,'7':5040,'8':40320,'9':362880}
    res = []
    return sum([numdcit.get(i) for i in list(str(valor))])
    
def p34():
    res=[]
    for i in range(3,1000000):
        if factsum(i)==i:
            res.append(i)
    return sum(res) 
    
print(p34())

