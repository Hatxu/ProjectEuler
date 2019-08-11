coins= { 1:1, 2:2 , 3:5 , 4:10 , 5:20 , 6:50 , 7:100 , 8:200 }
amount = 200
def ways ( target , avc ):
    if avc <= 1: 
        return 1
    res = 0
    while target >= 0:
        res = res + ways ( target , avc -1)
        target = target - coins [ avc ]
    return res
print (ways(200,8))

