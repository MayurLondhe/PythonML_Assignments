

def checkNoIsPosOrNeg(No1):
    Result = ""
    if(No1 > 0):
        Result = "Positive Number"
    elif(No1 < 0):
        Result = "Negative Number"
    else:
        Result = "Zero"
    
    return Result

def main():

    No = int(input("Enter a number : "))

    ret = checkNoIsPosOrNeg(No1 = No)

    print(ret)

if(__name__ == "__main__"):
    main()