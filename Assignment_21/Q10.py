import threading

Sum = 0
Product = 1

def sumOfList(DataIn):

    global Sum

    for i in range(0,len(DataIn),1):
        Sum = Sum + DataIn[i]


def productOfList(DataIn):

    global Product

    for i in range(0,len(DataIn),1):
        Product = Product * DataIn[i]
        

def main():

    Data = [1,2,3,4,5,6,7,8,9,10,11,12]

    sumOfListList = threading.Thread(target=sumOfList, args=(Data,))
    productOfListList = threading.Thread(target=productOfList, args=(Data,))

    sumOfListList.start()
    productOfListList.start()

    sumOfListList.join()
    productOfListList.join()

    print("Sum of element is : ", Sum)
    print("Product of element is : ", Product)

    print("Exit from main")

if(__name__ == "__main__"):
    main()


