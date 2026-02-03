import os

def main():
    
    FileName = input("Enter a file name : ")
    
    Ret = os.path.exists(FileName)

    if(Ret):

        fobj = open(FileName,"r")

        Data = fobj.read()

        print(Data)
        fobj.close()
    
    else:
        print(f"{FileName} not exixts.")
        
    

if(__name__ == "__main__"):
    main()