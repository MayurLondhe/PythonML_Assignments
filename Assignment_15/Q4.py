from functools import reduce

lstOfAddition = lambda No1, N02 : No1 + N02


def main():

    Data = [3,6,5,16]

    RData = reduce(lstOfAddition, Data)

    print(RData)

if __name__ == "__main__":
    main()