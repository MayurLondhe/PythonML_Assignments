

def manyRevNumbers(Value):
    Result = ""
    for i in range(Value,0,-1):
        Result = Result + str(i)
    return Result


def main():
    
    No1 = int(input("Enter a number : "))

    ret = manyRevNumbers(No1)
    print(ret)


if __name__ == "__main__":
    main()