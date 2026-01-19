
def calArea(Radius):
    Area = 0

    Area = 3.14 * Radius ** 2

    return Area

def main():

    Radius = int(input("Enter the radius : "))

    ret = 0
    ret = calArea(Radius)

    print("Area is : ", ret)

if __name__ == "__main__":
    main()
