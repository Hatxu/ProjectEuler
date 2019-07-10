def letravar(palabra):  
  valor = 0
  valores = {'"':0,"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R"  :18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}
  for i in palabra:
    valor= valores.get(i)+valor
  return(valor)

fo = open("p022_names.txt", "rt")
lISTA = fo.read()
lISTA = sorted(lISTA.split(","))
final = []
for i in lISTA:
  final.append((lISTA.index(i)+1)*letravar(i))
print(sum(final))
