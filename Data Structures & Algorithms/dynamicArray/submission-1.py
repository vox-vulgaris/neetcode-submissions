class DynamicArray:
    
    # O(n)
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.array = [None] * capacity

    # O(1)
    def get(self, i: int) -> int:
        return self.array[i]

    # O(1)
    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    # On average, O(1); Worst-case, O(n)
    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
            self.array[self.size] = n
            self.size += 1
        else:
            self.array[self.size] = n
            self.size += 1

    # O(1)
    def popback(self) -> int:
        self.size -= 1
        popback_value = self.array[self.size]
        self.array[self.size] = None
        return popback_value
 
    # O(n)
    def resize(self) -> None:
        self.capacity *= 2
        new_array = [None] * self.capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array

    # O(1)
    def getSize(self) -> int:
        return self.size    
    
    # O(1)
    def getCapacity(self) -> int:
        return self.capacity