class MinStack:

    def __init__(self):
        self.stack = []
        self.helper = []
        
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.helper) == 0:
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
        if len(self.stack) == 0:
            return None
        return self.helper[-1]
        
