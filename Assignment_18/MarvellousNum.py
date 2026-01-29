
def checkPrime(Value):
    count = 0
    Result = False

    for i in range(1,Value+1,1):

        if Value % i == 0 :
            count = count + 1
        
    if count == 2:
        Result = True
    else:
        Result = False

    return Result