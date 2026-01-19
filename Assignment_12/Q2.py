

def main():

    no = int(input("Enter a number : "))
    result = ""

    for i in range(1,no+1):

        if no % i == 0:
            result = result + str(i)

    print(result)

if __name__ == "__main__":
    main()