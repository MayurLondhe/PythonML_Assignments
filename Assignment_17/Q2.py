
def main():

    No = int(input("Enter a number : "))

    for i in range(0, No, 1):
        for j in range(0, No, 1):
            print("*", end= "  ")
        print("")

if (__name__ == "__main__"):
    main()