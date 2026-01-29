
def displayStar(Count):

    for _ in range(0, Count, 1):
        print("*", end= " ")

def main():
    CountValue = int(input("Enter a number : "))

    displayStar(CountValue)

if(__name__ == "__main__"):
    main()