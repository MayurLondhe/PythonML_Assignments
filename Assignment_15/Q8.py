
lstOfNoDivi3Or5 = lambda No1 : No1 % 3 == 0 or No1 % 5 == 0


def main():

    Data = [6,25,8,10]

    FData = list(filter(lstOfNoDivi3Or5, Data))

    print(FData)

if __name__ == "__main__":
    main()