def power(a,b):
    x = []
    for i in range(a,b+1):
        for j in range(a,b+1):
            w = i**j
            if w not in x:
                x.append(w)
                
    return sorted(x)

print(len(power(2,100)))
