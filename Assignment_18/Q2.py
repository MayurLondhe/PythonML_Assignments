
def checkMaximumNo(Data):

    max = Data[0]

    for i in range(0, len(Data), 1):

        if (Data[i] > max):
            max = Data[i]

        
    return max


def main():

    lenght = int(input("Enter a length of list : "))

    Data = list()

    for _ in range(0, lenght, 1):
        Value = int(input())
        Data.append(Value)

    MaximumNo = checkMaximumNo(Data)

    print(MaximumNo)

if (__name__ == "__main__"):
    main()