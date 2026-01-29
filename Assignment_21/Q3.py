import threading

Counter = 0
lobj = threading.Lock()

def IncreamentCounter():
    global Counter

    for _ in range(0, 2000000, 1):
        with lobj:
            Counter = Counter + 1


def main():

    global Counter

    T1 = threading.Thread(target=IncreamentCounter)
    T2 = threading.Thread(target=IncreamentCounter)

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("Value of Counter is : ", Counter)

if(__name__ == "__main__"):
    main()