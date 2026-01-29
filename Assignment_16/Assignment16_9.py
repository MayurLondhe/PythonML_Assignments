
def displayFirst10Even():

    count = 0
    Increament = 1
    Start = True
    while(Start):

        if(Increament % 2 == 0):
            print(Increament, end= " ")
            count = count + 1

        Increament  = Increament + 1
        
        if(count == 10):
            Start = False
        

def main():

    displayFirst10Even()

if(__name__ == "__main__"):
    main()