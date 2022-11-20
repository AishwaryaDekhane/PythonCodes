import os

def createFile(filename):
    if(os.path.exists(filename)):
        print("File is already existing ")
    else:
        fd = open(filename,"w")


def main():
    print("Enter the filename to create ")
    name = input()

    createFile(name)

if __name__ == "__main__":
    main()