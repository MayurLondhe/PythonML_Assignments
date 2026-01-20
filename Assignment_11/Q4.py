
def revNumber(Value):

    Rev = 0

    i = Value

    while i > 0:

        Rev = (Rev * 10) + i % 10
        i = i // 10

    return Rev

def main():

    No = int(input("Enter a number for reverse : "))

    No = revNumber(No)

    print(No)

if __name__ == "__main__":
    main()
