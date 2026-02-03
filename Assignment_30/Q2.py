import os
import sys

def CountOfWords(FileName1):
        fobj = open(FileName1,"r")

        Data = fobj.read()
        Data = Data.split(" ")

        Count = len(Data)
  
        fobj.close()
        return Count

def main():
    
    if(len(sys.argv) != 2):
        print("Invalid input parameters.")
        return
        
    FileExists = os.path.exists(sys.argv[1])

    FileName = sys.argv[1]

    if(FileExists):

        ret = CountOfWords(FileName)

        print(f"Total number of words in {FileName} is {ret}.")
    else:
        print("file not exixts.")
    

if(__name__ == "__main__"):
    main()