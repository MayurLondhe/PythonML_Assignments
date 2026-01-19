
def calArea(Lenght,Width):
    Area = 0

    Area = Lenght * Width

    return Area

def main():

    Lenght = int(input("Enter the lenght : "))
    Width = int(input("Enter the with : "))

    ret = 0
    ret = calArea(Lenght,Width)

    print("Area is : ", ret)

if __name__ == "__main__":
    main()
