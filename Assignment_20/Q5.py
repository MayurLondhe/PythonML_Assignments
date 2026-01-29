import threading

def thread1():

    for i in range(1, 51, 1):
        print(i)

    print("Thread 1 is complited")

def thread2():

    for i in range(50, 0, -1):
        print(i)    
        
    print("Thread 2 is complited")


def main():

    Thread1 = threading.Thread(target=thread1)
    Thread2 = threading.Thread(target=thread2)

    Thread1.start()
    Thread1.join()

    Thread2.start()
    Thread2.join()


    print("Exit from main")

if(__name__ == "__main__"):
    main()


