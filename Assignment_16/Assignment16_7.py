
def checkNoIsDiviBy5(No):
    Result = False

    if(No % 5 == 0):
        Result = True
    else:
        Result = False

    return Result

def main():

    No = int(input("Enter a number : "))

    ret = checkNoIsDiviBy5(No)

    print(ret)

if(__name__ == "__main__"):
    main()
