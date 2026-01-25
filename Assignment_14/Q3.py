
findMaxNo = lambda No1, No2 : No2 if (No1 < No2) else No1

def main():

    print("Enter the two number.")

    Value1 = int(input())
    Value2 = int(input())


    ret = findMaxNo(Value1, Value2)
    print("Maximum number is : ",ret)


if __name__ == "__main__":
    main()

