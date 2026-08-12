class MinStack:

    def __init__(self):
        self.stack = []
        self.helper = []
        
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.helper:
            self.helper.append(val)
        elif val <= self.helper[-1]:
            self.helper.append(val)
        

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.helper[-1]:
            self.helper.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        if not self.stack:
            return None
        return self.helper[-1]
        
