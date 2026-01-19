
def checkPerfectNo(Value):

    temp = 0
    Result = False
    for i in range(1,Value,1):

        if(Value%i == 0):
            temp = temp + i
            
    if(temp == Value):
        Result = True
    else:
        Result = False

    return Result
    
def main():

    No1 = int(input("Enter a number : "))

    ret = checkPerfectNo(No1)

    if(ret):
        print("Perfect number")

    else:
        print("Not a perfect number")

if __name__ == "__main__":
    main()