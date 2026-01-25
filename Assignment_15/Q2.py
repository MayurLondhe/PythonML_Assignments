
lstOfEven = lambda No1 : No1 % 2 == 0


def main():

    Data = [3,6,5,16]

    FData = list(filter(lstOfEven, Data))

    print(FData)

if __name__ == "__main__":
    main()