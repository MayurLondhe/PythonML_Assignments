

findMaxNo = lambda No1, No2, No3 : No1 if (No1 > (No2 if (No2 > No3) else No3)) else (No2 if (No2 > No3) else No3)

def main():

    print("Enter the two number.")

    Value1 = int(input())
    Value2 = int(input())
    Value3 = int(input())


    ret = findMaxNo(Value1, Value2, Value3)

    print("Largest number is : ",ret)


if __name__ == "__main__":
    main()

