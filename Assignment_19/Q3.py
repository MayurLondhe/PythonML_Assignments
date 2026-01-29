
def filter(Data):

    FData = []

    for i in range(0, len(Data), 1):

        if(Data[i] >= 70 and Data[i] <= 90):
            FData.append(Data[i])

    return FData

def map(Data):

    MData = []

    for i in range(0, len(Data), 1):
        MData.append(Data[i] + 10)

    return MData

def reduce(Data):

    RData = 1

    for i in range(0, len(Data), 1):
        RData = RData * Data[i]

    return RData


def main():

    # Data = [4,34,36,76,68,24,89,23,23,86,90,45,70]

    lenght = int(input("Enter a length of list : "))

    Data = list()

    for _ in range(0, lenght, 1):
        Value = int(input())
        Data.append(Value)

    FData = filter(Data)
    print("List of filter = ", FData)
    MData = map(FData)
    print("List of map = ", MData)
    RData = reduce(MData)
    print("Output of reduce = ", RData)

if __name__ == "__main__":
    main()

    