from File import File

class Folder:
    def __init__(self, rootDir = [], name = "", size = 0, subdirs = [], files = []):
        self.name = name
        self.size = size
        self.subdirs = subdirs
        self.rootDir = rootDir
        self.files = files
    def addSubDir(self, name = ""):
        self.subdirs.append(Folder(rootDir=self, name=name))
    def addFile(self, name = "", size = 0):
        self.files.append(File(name, size))
        self.size += size
        self.calcSize()
    def changeSize(self, size = 0):
        if self.rootDir != None:
            self.size = size
            self.rootDir.calcSize()
    def calcSize(self):
        self.size = 0
        for dir in self.subdirs:
            self.size += dir.size
        for file in self.files:
            self.size += file.size
        if self.rootDir != None:
            self.rootDir.calcSize()