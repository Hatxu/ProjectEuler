def selpower():
    return str(sum([i**i for i in range(1,1000+1)]))[-10::]
print(selpower())    

