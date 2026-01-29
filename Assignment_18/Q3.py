
def checkMinimumNo(Data):

    min = Data[0]

    for i in range(0, len(Data), 1):

        if (Data[i] < min):
            min = Data[i]

        
    return min


def main():

    lenght = int(input("Enter a length of list : "))

    Data = list()

    for _ in range(0, lenght, 1):
        Value = int(input())
        Data.append(Value)

    Minimum = checkMinimumNo(Data)

    print(Minimum)

if (__name__ == "__main__"):
    main()