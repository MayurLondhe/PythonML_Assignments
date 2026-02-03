import os
import sys

def CountOfLines(FileName1):
        fobj = open(FileName1,"r")

        Data = fobj.readlines()
        countOfLines = len(Data)
        
        fobj.close()
        return countOfLines

def main():
    
    if(len(sys.argv) != 2):
        print("Invalid input parameters.")
        return
        
    FileExists = os.path.exists(sys.argv[1])

    FileName = sys.argv[1]

    if(FileExists):

        ret = CountOfLines(FileName)

        print(f"Total number of Lines in {FileName} is {ret}.")
    else:
        print("file not exixts.")
    

if(__name__ == "__main__"):
    main()