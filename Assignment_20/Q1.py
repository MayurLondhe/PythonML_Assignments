import threading

def displayEven():

    Count = 0
    Element = 1
    print("Below is even numbers")
    while(Count < 10):

        if(Element % 2 == 0):

            print(Element)

            Count = Count + 1
        
        Element = Element + 1

def displayOdd():

    Count = 0
    Element = 1
    print("Below is odd numbers")
    while(Count < 10):

        if(Element % 2 != 0):

            print(Element)

            Count = Count + 1
        
        Element = Element + 1

def main():

    Even = threading.Thread(target=displayEven)
    Odd = threading.Thread(target=displayOdd)

    Even.start()
    Odd.start()

    print("Exit from main")

if(__name__ == "__main__"):
    main()


