import threading

def primeList(DataIn):

    PrimeData = []

    for i in range(0,len(DataIn),1):
        count = 0
        for j in range(1,DataIn[i]+1,1):

            if DataIn[i] % j == 0 :
                count = count + 1
            
        if count == 2:
            PrimeData.append(DataIn[i])
            

    print("Prime Numbers are : ",PrimeData)


def nonPrimeList(DataIn):

    PrimeData = []

    for i in range(0,len(DataIn),1):
        count = 0
        for j in range(1,DataIn[i]+1,1):

            if DataIn[i] % j == 0 :
                count = count + 1
            
        if count != 2:
            PrimeData.append(DataIn[i])

    print("Non-Prime Numbers are : ",PrimeData)

def main():

    Data = [1,2,3,4,5,6,7,8,9,10,11,12]

    PrimeList = threading.Thread(target=primeList, args=(Data,))
    NonPrimeList = threading.Thread(target=nonPrimeList, args=(Data,))

    PrimeList.start()
    NonPrimeList.start()

    PrimeList.join()
    NonPrimeList.join()

    print("Exit from main")

if(__name__ == "__main__"):
    main()


