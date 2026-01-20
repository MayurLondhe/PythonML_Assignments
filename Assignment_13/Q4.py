# print(8//2)
# print(8%2)


# print(4//2)
# print(4%2)

# print(2//2)
# print(2%2)

# print(1//2)
# print(1%2)

# print(7//2)
# print(7%2)

# print(3//2)
# print(3%2)

# print(1//2)
# print(1%2)

def IntToBinary(Value):
    tempBinary = list()
    i = Value
    while i > 0:
        tempBinary.append(i%2)
        i = i//2
        
    Binary = list()
    for i in range(len(tempBinary)-1,-1,-1):
        Binary.append(tempBinary[i])

    return Binary

def main():

    No = int(input("Enter a number : "))

    Ret = IntToBinary(No)

    print(Ret)

if __name__ == "__main__":
    main()


