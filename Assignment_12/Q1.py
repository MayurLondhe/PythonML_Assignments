
def main():

    ch = input("Enter a alphabet : ")
    print(len(ch))
    if  len(ch) == 1 and (ch == 'A' or ch == 'a' or ch == 'E' or ch == 'e' or ch == 'I' or ch == 'i' or ch == 'O' or ch == 'o' or ch == 'U' or ch == 'u'):
        print("Vowel")
    else:
        print("Not a vowel")


if __name__ == "__main__":
    main()