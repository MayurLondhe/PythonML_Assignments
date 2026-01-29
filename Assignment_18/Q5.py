from MarvellousNum import checkPrime
from functools import reduce

def ListPrime(Data):
    LstPrimeData = []

    LstPrimeData = list(filter(checkPrime, Data))

    return LstPrimeData

addition = lambda No1, No2 : No1 + No2

def main():

    lenght = int(input("Enter a length of list : "))

    Data = list()

    for _ in range(0, lenght, 1):
        Value = int(input())
        Data.append(Value)

    PrimeList = ListPrime(Data)

    Addition = reduce(addition, PrimeList)

    print(Addition)

if (__name__ == "__main__"):
    main()