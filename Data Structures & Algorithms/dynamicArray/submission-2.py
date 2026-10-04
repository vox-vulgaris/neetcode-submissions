class DynamicArray:
    
    # O(n)
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.arr = [None] * self.capacity

    # O(1)
    def get(self, i: int) -> int:
        return self.arr[i]

    # O(1)
    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    # O(1) average, O(n) worst-case
    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
            self.arr[self.size] = n
            self.size += 1
        else:
            self.arr[self.size] = n
            self.size += 1

    # O(1)
    def popback(self) -> int:
        self.size -= 1
        popback_element = self.arr[self.size]
        self.arr[self.size] = None
        return popback_element

    # O(n)
    def resize(self) -> None:
        self.capacity *= 2
        new_arr = [None] * self.capacity
        for i in range(self.size):
            new_arr[i] = self.arr[i]
            self.arr[i] = None
        self.arr = new_arr

    # O(1)
    def getSize(self) -> int:
        return self.size
    
    # O(1)
    def getCapacity(self) -> int:
        return self.capacity