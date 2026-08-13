class Deque:
    class ListNode:
        def __init__(self, prev=None, val=0, next=None):
            self.prev = prev
            self.val = val
            self.next = next

    
    def __init__(self):
        self.head = None
        self.tail = None


    def isEmpty(self) -> bool:
        return self.head == None
        

    def append(self, value: int) -> None:
        if self.isEmpty():
            self.head = self.ListNode(None, value, None)
            self.tail = self.head
            return
        newTail = self.ListNode(self.tail, value, None)
        self.tail.next = newTail
        self.tail = self.tail.next

        
        

    def appendleft(self, value: int) -> None:
        if self.isEmpty():
            self.head = self.ListNode(None, value, None)
            self.tail = self.head
            return
        newHead = self.ListNode(None, value, self.head)
        self.head.prev = newHead
        self.head = self.head.prev

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        if self.head == self.tail:
            val = self.head.val
            self.head = None
            self.tail = None
            return val
        val = self.tail.val
        self.tail.prev.next = None
        self.tail = self.tail.prev
        return val    

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        if self.head == self.tail:
            val = self.head.val
            self.head = None
            self.tail = None
            return val
        val = self.head.val
        self.head.next.prev = None
        self.head = self.head.next
        return val

        
