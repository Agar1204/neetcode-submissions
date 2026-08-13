class BrowserHistory:
    class PageNode:
        def __init__(self, prev=None, val="", next=None):
            self.prev = prev
            self.val = val
            self.next = next

    def __init__(self, homepage: str):
        self.head = self.PageNode(None, homepage, None)
        self.curr = self.head
        

    def visit(self, url: str) -> None:
        newPage = self.PageNode(self.curr, url, None)
        self.curr.next = newPage
        self.curr = self.curr.next

    def back(self, steps: int) -> str:
        num_steps = 0
        while num_steps < steps and self.curr.prev != None:
            self.curr = self.curr.prev
            num_steps += 1
        return self.curr.val

    def forward(self, steps: int) -> str:
        num_steps = 0
        while num_steps < steps and self.curr.next != None:
            self.curr = self.curr.next
            num_steps += 1
        return self.curr.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)