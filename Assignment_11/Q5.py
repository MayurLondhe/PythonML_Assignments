
def checkPalindrome(Value1):
    RevValue = ""
    ret = False
    for i in range(len(Value1)-1,-1,-1):
        RevValue = RevValue + str(Value1[i])

    if(RevValue == Value1):
        ret = True
    else:
        ret = False

    return ret
        


def main():
    
    No = input("Enter Number : ")

    ret = checkPalindrome(No)
    
    if(ret):
        print("Palindrome")
    else:
        print("Not Palindrome")

    
    
if __name__ == "__main__":
    main()