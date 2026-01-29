
def checkLenghtOfNo(Value):

    i = Value
    count = 0

    while i > 0:
        i = i // 10
        count = count + 1

    return count

def main():

    No = int(input("Enter a number : "))

    No = checkLenghtOfNo(No)

    print(No)

if __name__ == "__main__":
    main()


    
