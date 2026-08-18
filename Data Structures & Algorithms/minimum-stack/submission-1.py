class MinStack:

    def __init__(self):
        self.arr = []
        self.stack_min = []

    def push(self, val: int) -> None:
        self.arr.append(val)
        if(self.stack_min):
            min_val = min(self.stack_min[-1],val)
        else:
            min_val = val
        self.stack_min.append(min_val)   

    def pop(self) -> None:
        self.arr.pop()
        self.stack_min.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.stack_min[-1]
        
