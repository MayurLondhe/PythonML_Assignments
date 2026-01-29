
def checkPrime(Value):
    count = 0
    Result = False

    for i in range(1,Value+1,1):

        if Value % i == 0 :
            count = count + 1
        
    if count == 2:
        Result = True
    else:
        Result = False

    return Result

def map(Data):

    MData = []

    for i in range(0, len(Data), 1):
        MData.append(Data[i] * 2)

    return MData

def reduce(Data):

    RData = Data[0]

    for i in range(0, len(Data), 1):
        if(Data[i] > RData):
            RData = Data[i]

    return RData


def main():

    # Data = [4,34,36,76,68,24,89,23,23,86,90,45,70]

    lenght = int(input("Enter a length of list : "))

    Data = list()

    for _ in range(0, lenght, 1):
        Value = int(input())
        Data.append(Value)

    FData = list(filter(checkPrime, Data))
    print("List of filter = ", FData)
    MData = map(FData)
    print("List of map = ", MData)
    RData = reduce(MData)
    print("Output of reduce = ", RData)

if __name__ == "__main__":
    main()

    