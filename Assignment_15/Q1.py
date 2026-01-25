
lstOfSqurt = lambda No1 : No1 ** 2


def main():

    Data = [3,6,5,16]

    MData = list(map(lstOfSqurt, Data))

    print(MData)

if __name__ == "__main__":
    main()