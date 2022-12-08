from Folder import Folder

f = open("7-input.txt")
maxDirSize = 100000
dirSum = 0
            
rootDirectory = Folder(name="/", rootDir=None)
currentDir = rootDirectory

def checkDirSize(folder = Folder()):
    global dirSum
    if folder.size <= maxDirSize:
        dirSum += folder.size

for line in f:
    if line[0] == "$":
        line = line.rstrip().split(" ")
        if line[1] == "cd":
            dir = line[2]
            if dir == "..":
                currentDir = currentDir.rootDir
            else:
                for f in currentDir.subdirs:
                    if f.name == dir:
                        currentDir = f
    else:
        line = line.rstrip().split(" ")
        if line[0] == "dir":
            dir = line[1]
            currentDir.addSubDir(dir)
        else:
            size = int(line[0])
            name = line[1]
            currentDir.addFile(name=name,size=size)




print(dirSum)