class MyLinkedList:
    class ListNode:
        def __init__(self, val=0, prev=None, next=None):
            self.val = val
            self.prev = prev
            self.next = next

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0     

    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.val
        
    def addAtHead(self, val: int) -> None:
        if not self.head:
            self.head = self.ListNode(val)
            self.tail = self.head
        else:
            self.head.prev = self.ListNode(val, None, self.head)
            self.head = self.head.prev
        self.length += 1

    def addAtTail(self, val: int) -> None:
        if not self.tail:
            self.head = self.ListNode(val)
            self.tail = self.head
        else:
            self.tail.next = self.ListNode(val, self.tail, None)
            self.tail = self.tail.next
        self.length += 1
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        elif index < 0 or index > self.length:
            return None
        else:
            curr = self.head
            for _ in range(index):
                curr = curr.next
            node = self.ListNode(val, curr.prev, curr)
            curr.prev.next = curr.prev = node
            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if 0 <= index < self.length:
            curr = self.head
            for _ in range(index):
                curr = curr.next
            if curr.prev:
                curr.prev.next = curr.next
            else:
                if curr.next:
                    self.head = curr.next
                    self.head.prev = None
                else:
                    self.head = self.tail = None
            if curr.next:
                curr.next.prev = curr.prev
            else:
                if curr.prev:
                    self.tail = curr.prev
                    self.tail.next = None
                else:
                    self.head = self.tail = None
            self.length -= 1