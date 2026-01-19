

def manyNumbers(Value):
    Result = ""
    for i in range(1,Value+1,1):
        Result = Result + str(i)
    return Result


def main():
    
    No1 = int(input("Enter a number : "))

    ret = manyNumbers(No1)
    print(ret)


if __name__ == "__main__":
    main()