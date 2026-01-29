
def additionOfAllNo(Value):

    sum = 0

    i = Value

    while i > 0:

        sum = sum + i % 10
        i = i // 10

    return sum

def main():

    No = int(input("Enter a number : "))

    No = additionOfAllNo(No)

    print(No)

if __name__ == "__main__":
    main()


    
