from functools import reduce

findMinNo = lambda No1, No2 : No2 if (No1 > No2) else No1


def main():

    Data = [3,66,5,1]

    RData = reduce(findMinNo, Data)

    print(RData)

if __name__ == "__main__":
    main()