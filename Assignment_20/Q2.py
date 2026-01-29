import threading

def evenFactor(Value1):

    sum = 0

    for i in range(1, Value1+1, 1):

        if(Value1 % i == 0):

            if(i % 2 == 0):

                sum = sum + i

    print("Sum of even factors : ",sum)


def oddFactor(Value1):

    sum = 0

    for i in range(1, Value1+1, 1):

        if(Value1 % i == 0):

            if(i % 2 != 0):

                sum = sum + i
    print("Sum of odd factors : ",sum)

def main():

    No = int(input("Enter a number : "))

    EvenFactor = threading.Thread(target=evenFactor, args=(No,))
    OddFactor = threading.Thread(target=oddFactor, args=(No,))

    EvenFactor.start()
    OddFactor.start()

    EvenFactor.join()
    OddFactor.join()

    print("Exit from main")

if(__name__ == "__main__"):
    main()


