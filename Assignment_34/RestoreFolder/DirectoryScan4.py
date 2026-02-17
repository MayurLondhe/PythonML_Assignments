import os
import demo

def DirectoryScanner(DirectoryName = "Marvellous"):
    print("Contents of a directory are : ")

    if(os.path.isdir(DirectoryName) == False):
        print("There is no such directory.")
        return

    if(os.path.exists(DirectoryName)):

        for FolderName, SubFolderName, FileName in os.walk(DirectoryName):

            print("Folder Name : ", FolderName)

            for subf in SubFolderName:
                print("Sub Folder Name : ", subf)

            for fname in FileName:
                print("File Name : ", fname)
                
    else:
        print("Directory not found")


def main():
    DirectoryName = input("Enter the name of directory : ")
    DirectoryScanner(DirectoryName)


if(__name__ == "__main__"):

    main()