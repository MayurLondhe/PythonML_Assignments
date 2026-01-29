import threading

def maxElement(DataIn):

    Max = DataIn[0]

    for i in range(0,len(DataIn),1):
        
        if(DataIn[i] > Max):
            Max = DataIn[i]

    print("Maximum Elemet is : ",Max)


def minElement(DataIn):

    Min = DataIn[0]

    for i in range(0,len(DataIn),1):
        
        if(DataIn[i] < Min):
            Min = DataIn[i]

    print("Minimum Element is : ",Min)

def main():

    Data = [40,2,3,4,5,25,7,8,1,10,11,12]

    MaximumElemt = threading.Thread(target=maxElement, args=(Data,))
    MinimumnElemt = threading.Thread(target=minElement, args=(Data,))

    MaximumElemt.start()
    MinimumnElemt.start()

    MaximumElemt.join()
    MinimumnElemt.join()

    print("Exit from main")

if(__name__ == "__main__"):
    main()


