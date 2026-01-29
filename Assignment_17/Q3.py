
def getFactorialNo(Value1):

    ret = 1

    for i in range(1, Value1+1, 1):
        ret = ret * i
    
    return ret

def main():
    No = int(input("Enter a number : "))

    Ans = getFactorialNo(No)

    print("Factorial number of given number is : ", Ans)

if (__name__ == "__main__"):
    main()