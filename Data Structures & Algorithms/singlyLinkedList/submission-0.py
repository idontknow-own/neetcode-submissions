class LinkedList:
    linkList = []

    def __init__(self):
        self.linkList = []

    
    def get(self, index: int) -> int:
        if index < len(self.linkList):
            return self.linkList[index]
        else:
            return -1

    def insertHead(self, val: int) -> None:
        self.linkList.insert(0, val)

    def insertTail(self, val: int) -> None:
        self.linkList.append(val)
        

    def remove(self, index: int) -> bool:
        if index >= len(self.linkList):
            return False
        else:
            self.linkList.pop(index)
            return True
        

    def getValues(self) -> List[int]:
        return self.linkList
