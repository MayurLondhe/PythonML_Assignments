import threading

def smallChar(Value):
    print("Inside display Small Thread ID : ", threading.get_ident())

    Count = 0

    for i in range(0, len(Value), 1):

        if(Value[i] >= 'a' and Value[i] <= 'z'):
           Count = Count + 1 

    print("Number of lower characters is Thread ID : ",Count)


def capChar(Value):
    print("Inside display Capital : ", threading.get_ident())

    Count = 0

    for i in range(0, len(Value), 1):

        if(Value[i] >= 'A' and Value[i] <= 'Z'):
           Count = Count + 1 

    print("Number of upper characters is Thread ID : ",Count)

def digitChar(Value):
    print("Inside display Digit : ", threading.get_ident())

    Count = 0

    for i in range(0, len(Value), 1):

        if(Value[i] >= '0' and Value[i] <= '9'):
           Count = Count + 1 

    print("Number of numeric digit is : ",Count)

def main():
    print("Inside display main Thread ID : ", threading.get_ident())

    String = "May33ur"

    Small = threading.Thread(target=smallChar, args=(String,))
    Capital = threading.Thread(target=capChar, args=(String,))
    Digits = threading.Thread(target=digitChar, args=(String,))

    Small.start()
    Capital.start()
    Digits.start()

    Small.join()
    Capital.join()
    Digits.join()

    print("Exit from main")

if(__name__ == "__main__"):
    main()


