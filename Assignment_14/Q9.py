
Addition = lambda No1, No2 : No1 * No2

def main():

    print("Enter the two number for multiplication.")

    Value1 = int(input())
    Value2 = int(input())


    ret = Addition(Value1, Value2)

    print("Multiplication of given number is : ",ret)

if __name__ == "__main__":
    main()