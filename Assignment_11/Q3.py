
def getSumOfDigit(Value1):
    Result = 0

    for i in range(0,len(Value1),1):
        Result = Result + int(Value1[i])
        
    return Result


def main():
    
    No = input("Enter Number : ")

    ret = getSumOfDigit(No)
    
    print("Sum of digit is : ", ret)
    
if __name__ == "__main__":
    main()