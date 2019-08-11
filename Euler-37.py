def prime(valor): #prime value function
    return True if 2**valor%valor == 2 or valor==2 else False
    
def circular(valor): #know if the cilcular of a number is prime
    x =  list(str(valor))
    res = []
    for i in range(len(x)):
        z = x.pop(0)
        x.append(z)
        res.append(int("".join(x)))
    for i in res:
        if prime(i) == False:
            return False
    return valor        


myfile = open("primos.txt", "rt") #list of the first 100000 prime values
contents = myfile.read()
content= contents.split(",")
x = [int(i) for i in content[1:-2]] #Here I clean up the txt

final = []
for i in x:
  j = circular(i)
  if j != False:
    print(j)
    final.append(j)
print(final,len(final))    
