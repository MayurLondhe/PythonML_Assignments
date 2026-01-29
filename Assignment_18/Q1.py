from functools import reduce

addition = lambda No1, No2 : No1 + No2

def main():

    lenght = int(input("Enter a length of list : "))

    Data = list()

    for _ in range(0, lenght, 1):
        Value = int(input())
        Data.append(Value)

    Addition = reduce(addition, Data)

    print(Addition)

if (__name__ == "__main__"):
    main()