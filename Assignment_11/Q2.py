
def getLength(Value1):
    Result = 0

    for i in range(1,len(Value1)+1,1):
        Result = Result + 1
        
    return Result


def main():
    
    No = input("Enter Number : ")

    ret = getLength(No)
    
    print("Count of digit is : ", ret)
    
if __name__ == "__main__":
    main()