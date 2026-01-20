
def displayEvenNo(Value1):
    print("Below are all even numbers :")
    for i in range(1,Value1+1,1):
        
        if i % 2 == 0:
            print(i)
        
    

def main():
    No1 = int(input("Enter a number : "))
    displayEvenNo(No1)

if __name__ == "__main__":
    main()