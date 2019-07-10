import datetime
        
def Contadomingos(fechain,fechafinal):
    counter=0
    for j in range(fechain,fechafinal+1):
        for i in range(1,13):
            if datetime.datetime(j,i,1).weekday() == 6:
                counter += 1 
    return counter
    
    
print(Contadomingos(1901,2000))    
