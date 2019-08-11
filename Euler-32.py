def pandigcal (a,b):
    res = a*b
    w = sorted(list(str(a))+list(str(b))+list(str(res)))
    if len(w) !=9:
        return 0
    if w ==['1','2','3','4','5','6','7','8','9']:
        return res

def pandigcalist():
    panda= []
    for i in range(9,99):
	    for j in range(99,999):
                pando = pandigcal(i,j)
                if pando not in panda and pando != None:
                    panda.append(pando)
                    
    for k in range(9):
	    for l in range(999,9999):
                pando = pandigcal(k,l)
                if pando not in panda and pando != None:
                    panda.append(pando)
                    
    return panda,sum(panda)
     
print(pandigcalist())    

