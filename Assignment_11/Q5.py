from Q4 import revNumber


def checkPalindrome(Value1):
    Result = False

    revNo = revNumber(Value1)

    if(revNo == Value1):
        Result = True
    else:
        Result = False

    return Result
        


def main():
    
    No = int(input("Enter Number : "))

    ret = checkPalindrome(No)
    
    if(ret):
        print("Palindrome")
    else:
        print("Not Palindrome")

    
    
if __name__ == "__main__":
    main()