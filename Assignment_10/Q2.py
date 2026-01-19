
def sumFirstNaturalNo(Value1):
    sum = 0
    for i in range(1,Value1+1,1):
        sum = sum + i
        
    return sum
    

def main():
    No1 = int(input("Enter a number : "))
    ret = 0
    ret = sumFirstNaturalNo(No1)
    
    print("Sum of first n natural number is : ", ret)

if __name__ == "__main__":
    main()