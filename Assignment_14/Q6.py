
isEven = lambda No1 : No1 % 2 == 0

def main():

    No = int(input("Enter a number : "))

    ret = isEven(No)

    print(ret)

if __name__ == "__main__":
    main()