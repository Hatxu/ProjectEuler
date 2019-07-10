def sumdiv(a):
    return sum([i for i in range(1,a) if a%i==0])
    
def amicable(a):
    lista=[]
    for i in range(1,a+1):
        if i not in lista:
            otro=sumdiv(i)
            if sumdiv(otro) == i and i != otro:
                print(i)
                lista.append(i)
                lista.append(otro)
    return lista,sum(lista)

print(amicable(10000))
