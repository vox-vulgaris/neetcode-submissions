class MinStack:

    def __init__(self):
        self.stack = []
        self.size = 0  
        self.min_stack = []      

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.size == 0:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[self.size - 1]))
        self.size += 1

    def pop(self) -> None:        
        self.size -= 1
        del self.stack[self.size]
        del self.min_stack[self.size]
        # self.stack[self.size] = None
        # self.min_stack[self.size] = None

    def top(self) -> int:
        return self.stack[self.size - 1]

    def getMin(self) -> int:        
        return self.min_stack[self.size - 1]
