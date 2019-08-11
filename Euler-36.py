def palbin(x):
    x = bin(x)[2:]
    return True if x == x[::-1] else False
    
def doublepal(x):
    res = []
    for i in range(1,x+1):
        if str(i) == str(i)[::-1]:  # this way I think is faster, because if the number is not a palindrome                       
            if palbin(i):   # you don't need to check he's binary number
                res.append(i)
    return res, sum(res)  
    
print(doublepal(1000000))    
    
