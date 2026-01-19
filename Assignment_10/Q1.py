
def displayMultiplication(Value1):
    
    for i in range(1,11,1):
        print(Value1*i)
    

def main():
    No1 = int(input("Enter number for multiplication table : "))
    displayMultiplication(No1)

if __name__ == "__main__":
    main()