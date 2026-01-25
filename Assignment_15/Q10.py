from Q2 import lstOfEven
from functools import reduce

countOfEvenNo = lambda No1, No2 : No1 + No2


def main():

    Data = [1,2,3,4,5,6]

    FData = list(filter(lstOfEven, Data))

    RData = reduce(countOfEvenNo,FData)

    print(RData)

if __name__ == "__main__":
    main()