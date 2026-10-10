class DynamicArray:
    array = []
    currentCap = 0

    def __init__(self, capacity: int):
        self.array = []
        self.currentCap = capacity

    def get(self, i: int) -> int:
        return self.array[i]


    def set(self, i: int, n: int) -> None:
        self.array[i] = n


    def pushback(self, n: int) -> None:
        self.array.append(n)
        if len(self.array) > self.currentCap:
            self.resize()

    def popback(self) -> int:
        return self.array.pop()
 

    def resize(self) -> None:
        self.currentCap *= 2


    def getSize(self) -> int:
        return len(self.array)
        
    
    def getCapacity(self) -> int:
        return self.currentCap
