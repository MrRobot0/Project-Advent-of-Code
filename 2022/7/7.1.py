from Folder import Folder
from File import File

f = open("D:\OneDrive\OneDrive - Office 365 Fontys\______________\Projects\Project Advent of Code\\2022\\7\\7-input.txt")
maxDirSize = 100000
dirSum = 0
debug = False
            
rootDirectory = Folder(name="/", rootDir=None)
currentDir = rootDirectory

def checkDirSize(folder = Folder()):
    global dirSum
    if folder.size <= maxDirSize:
        dirSum += folder.size

print("--------={ BEGIN }=--------")
for line in f:
    if line[0] == "$":
        line = line.rstrip().split(" ")
        if line[1] == "cd":
            dir = line[2]
            if dir == "/":
                currentDir = rootDirectory
                continue
            if dir == "..":
                if currentDir.rootDir != None:
                    currentDir = currentDir.rootDir
            else:
                for f in currentDir.subdirs:
                    if f.name == dir:
                        currentDir = f
                        break
    else:
        line = line.rstrip().split(" ")
        if line[0] == "dir":
            dir = line[1]
            currentDir.addSubDir(dir, debug=debug)
        else:
            size = int(line[0])
            name = line[1]
            currentDir.addFile(name=name,size=size, debug=debug)

print(dirSum)