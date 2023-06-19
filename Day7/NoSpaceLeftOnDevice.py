from enum import Enum
from typing import List

class FileType(Enum):
    DIR = 0
    FILE = 1

class FileNode:

    def __init__(self, name, type: FileType, parentName='', children=None, size=0):
        self.name = name
        self.fileType = type
        self.size = size
        self.children = children
        self.parentName = parentName

    def __str__(self):
        if self.fileType == FileType.FILE:
            info = f'(file, size={self.size})'
        else: info = '(dir)' 
        tree = f"- [Parent: {self.parentName}] {self.name} {info} "

        if self.children != None:
            for kid in self.children:
                tree += "\n\t" + kid.__str__()
        
        return tree
    
    def getSize(self):
        if self.fileType == FileType.FILE:
            return self.size
        
        totalSize = 0
        if self.children != None:
            for child in self.children:
                totalSize += child.getSize()

        return totalSize

    def getChildNode(self, toFindName):
        if self.name == toFindName: return self

        if self.children == None: return None

        for node in self.children:
            search = node.getChildNode(toFindName)
            if search != None:
                return search

class FilesystemManager:
    
    currNode = None

    def __init__(self):
        self.rootNode = FileNode('/', FileType.DIR)
        self.currNode = self.rootNode

    def changeDir(self, name):
        if (name == '..'):
            searchName = self.currNode.parentName
            self.currNode = self.rootNode.getChildNode(searchName)
        else:
            self.currNode = self.rootNode.getChildNode(name)

        if self.currNode is None:
            raise Exception(f"Child Not exist: {name}")
    
    def handleChilds(self, newKids: List[str]):
        
        for kid in newKids:
            data = kid.split(' ')
            if 'dir' in data[0]:
                newNode = FileNode(data[-1], FileType.DIR, self.currNode.name)
            else: #file
                size = int(data[0])
                newNode = FileNode(data[-1], FileType.FILE, self.currNode.name, None, size)

            if self.currNode.children is None:
                self.currNode.children = [newNode]
            else: self.currNode.children.append(newNode)
    
    def sumDirsOfMaxSize(self, node: FileNode, maxSize):
        size = 0
        if node.getSize() <= maxSize:
            size = node.getSize()
        
        if node.children != None:
            for kid in node.children:
                sumDirsOfMaxSize
            
            



def parseInput(filename):
    manager = FilesystemManager()
    with open(filename) as file:
        while(line := file.readline().rstrip()):
            if 'cd' in line:
                dirName = line.split(' ')[-1]
                manager.changeDir(dirName)
            elif 'ls' in line:
                childs = []
                while(listDirLine := file.readline().rstrip()):
                    seper = listDirLine.split(' ')
                    if seper[0] == '$': 
                        manager.handleChilds(childs)
                        dirName = seper[-1]
                        manager.changeDir(dirName)
                        childs = []
                        break
                    else:
                        childs.append(listDirLine)
                if childs != []:
                    manager.handleChilds(childs)

    print(manager.rootNode)                
                
if __name__ == "__main__":
    parseInput('test.txt')