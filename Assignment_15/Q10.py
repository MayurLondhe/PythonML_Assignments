from Q2 import lstOfEven

def main():

    Data = [1,2,3,4,5,6]

    FData = list(filter(lstOfEven, Data))

    print(len(FData))

if __name__ == "__main__":
    main()