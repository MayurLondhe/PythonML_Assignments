

multi = lambda No1, No2 : No1 * No2

def main():
    
    print("Enter the two number : ")
    No1 = int(input())
    No2 = int(input())

    ret = multi(No1, No2)

    print(ret)

if __name__ == "__main__":
    main()