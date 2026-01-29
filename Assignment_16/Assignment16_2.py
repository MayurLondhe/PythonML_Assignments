
def ChkNum(No1):

    if(No1 % 2 == 0):
        print("Even number")
    else:
        print("Odd number")

def main():

    No = int(input("Enter a number : "))

    ChkNum(No)

if(__name__ == "__main__"):
    main()