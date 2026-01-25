from functools import reduce

productOfNo = lambda No1, No2 : No1 * No2


def main():

    Data = [1,2,3,4]

    FData = reduce(productOfNo, Data)

    print(FData)

if __name__ == "__main__":
    main()