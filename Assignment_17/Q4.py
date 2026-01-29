def getAdditionOfFactors(Value1):

    ret = 0

    for i in range(1, Value1, 1):

        if(Value1 % i == 0):
            ret = ret + i
    
    return ret

def main():
    No = int(input("Enter a number : "))

    Ans = getAdditionOfFactors(No)

    print("Addition of its factors is : ", Ans)

if (__name__ == "__main__"):
    main()