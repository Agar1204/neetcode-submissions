class MyLinkedList:
    class LinkedListNode:
        def __init__(self, prev=None, val=0, next=None):
            self.prev = prev
            self.val = val
            self.next = next

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index: int) -> int:
        if index < 0 or index > self.length - 1:
            return -1
        curr = self.head
        currIndex = 0
        while currIndex != index:
            curr = curr.next
            currIndex += 1
        return curr.val
        

    def addAtHead(self, val: int) -> None:
        newHead = self.LinkedListNode(None, val, self.head)
        if self.length > 0:
            self.head.prev = newHead
        else:
            self.tail = newHead
        self.head = newHead
        self.length += 1
        

    def addAtTail(self, val: int) -> None:
        if self.length == 0:
            self.addAtHead(val)
            return
        newTail = self.LinkedListNode(self.tail, val, None)
        self.tail.next = newTail
        self.tail = newTail
        self.length += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        elif index == self.length:
            self.addAtTail(val)
            return
        if index < 0 or index >= self.length:
            return

        currIndex = 0
        curr = self.head
        prev = None
        while currIndex != index:
            prev = curr
            curr = curr.next
            currIndex += 1
        newNode = self.LinkedListNode(prev, val, curr)
        prev.next = newNode
        curr.prev = newNode
        self.length += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return 
        currIndex = 0
        curr = self.head
        prev = None
        while currIndex != index:
            prev = curr
            curr = curr.next
            currIndex += 1
        if prev == None:
            self.head = curr.next
            if self.head:
                self.head.prev = None
        else:
            prev.next = curr.next
        if index == self.length - 1:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            curr.next.prev = prev
        self.length -= 1
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)