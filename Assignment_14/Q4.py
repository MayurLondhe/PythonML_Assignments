
findMinNo = lambda No1, No2 : No1 if (No1 < No2) else No2

def main():

    print("Enter the two number.")

    Value1 = int(input())
    Value2 = int(input())


    ret = findMinNo(Value1, Value2)

    print("Minimum number is : ",ret)


if __name__ == "__main__":
    main()

