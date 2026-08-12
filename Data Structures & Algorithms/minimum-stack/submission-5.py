class MinStack:

    def __init__(self):
        self.stack = []
        self.helper = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.helper or val < self.helper[-1]:
            self.helper.append(val)
        else:
            self.helper.append(self.helper[-1])
        

    def pop(self) -> None:
        self.stack.pop(-1)
        self.helper.pop(-1)
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.helper[-1]
