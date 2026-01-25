
isDivisible5 = lambda No1 : No1 % 5 == 0

def main():

    No = int(input("Enter a number : "))

    ret = isDivisible5(No)

    print(ret)

if __name__ == "__main__":
    main()