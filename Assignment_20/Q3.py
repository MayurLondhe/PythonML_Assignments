import threading

def evenList(DataIn):

    sum = 0

    for i in range(0, len(DataIn), 1):

        if(DataIn[i] % 2 == 0):
            sum = sum + DataIn[i]

    print("Sum of even : ",sum)


def oddList(DataIn):

    sum = 0

    for i in range(0, len(DataIn), 1):

        if(DataIn[i] % 2 != 0):
            sum = sum + DataIn[i]

    print("Sum of odd : ",sum)

def main():

    Data = [1,2,3,4,5,6,7,8,9,10,11,12]

    EvenList = threading.Thread(target=evenList, args=(Data,))
    OddList = threading.Thread(target=oddList, args=(Data,))

    EvenList.start()
    OddList.start()

    EvenList.join()
    OddList.join()

    print("Exit from main")

if(__name__ == "__main__"):
    main()


