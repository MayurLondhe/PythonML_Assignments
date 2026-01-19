
def getFactorialNo(Value1):
    Fact = 1
    for i in range(1,Value1+1,1):
        Fact = Fact * i
        
    return Fact
    

def main():
    No1 = int(input("Enter a number : "))
    ret = 0
    ret = getFactorialNo(No1)
    
    print("Factorial number is : ", ret)

if __name__ == "__main__":
    main()