
cube = lambda No1 : No1 ** 3

def main():

    No = int(input("Enter a number : "))

    ret = 0
    ret = cube(No)

    print("Cube of given number is : ", ret)

if __name__ == "__main__":
    main()