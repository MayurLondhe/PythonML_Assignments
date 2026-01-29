
def checkFrequencyOfNo(Data, No):

    count = 0

    for i in range(0, len(Data), 1):

        if (Data[i] == No):
            count = count + 1

        
    return count


def main():

    lenght = int(input("Enter a length of list : "))

    Data = list()

    for _ in range(0, lenght, 1):
        Value = int(input())
        Data.append(Value)

    Number = int(input("Enter number to search : "))
    Count = checkFrequencyOfNo(Data, Number)

    print(Count)

if (__name__ == "__main__"):
    main()