
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

def main():
    
    No = int(input("Enter a number : "))

    ret = checkPrime(No)

    if(ret):
        print("Prime Number.")
    else:
        print("Not a prime number.")

if __name__ == "__main__":
    main()