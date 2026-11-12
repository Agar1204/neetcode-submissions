class BrowserHistory:
    class ListNode:
        def __init__(self, val="", prev=None, next=None):
            self.val = val
            self.prev = prev
            self.next = next

    def __init__(self, homepage: str):
        self.head = self.ListNode(homepage)
        self.curr = self.head

    def visit(self, url: str) -> None:
        self.curr.next = self.ListNode(url, self.curr)
        self.curr = self.curr.next    

    def back(self, steps: int) -> str:
        currSteps = 0
        while currSteps < steps and self.curr.prev:
            self.curr = self.curr.prev
            currSteps+=1
        return self.curr.val     

    def forward(self, steps: int) -> str:
        currSteps = 0
        while currSteps < steps and self.curr.next:
            self.curr = self.curr.next
            currSteps+=1
        return self.curr.val