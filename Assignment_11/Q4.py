
def getRevDigit(Value1):
    result = ""
    for i in range(len(Value1)-1,-1,-1):
        result = result + str(Value1[i])

    return result
        


def main():
    
    No = input("Enter Number : ")

    ret = getRevDigit(No)

    print(ret)
    
    
if __name__ == "__main__":
    main()