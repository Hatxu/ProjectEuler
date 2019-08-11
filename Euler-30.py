def allnumber(a):
    return sum([int(i)**5 for i in list(str(a))])
    
    
def digitfifht():
    lista5 = []
    for i in range(5,1000001):
        if allnumber(i) == i:
            lista5.append(i)
    return lista5,sum(lista5)
    
print(digitfifht())    
