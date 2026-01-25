
findStrHaveLen5 = lambda str1 : len(str1) > 5


def main():

    Data = ["Sagar", "Rahul","Mayur","Devarshi"]

    FData = list(filter(findStrHaveLen5, Data))

    print(FData)

if __name__ == "__main__":
    main()