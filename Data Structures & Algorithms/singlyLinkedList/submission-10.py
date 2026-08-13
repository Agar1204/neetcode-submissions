class LinkedList:
    class LinkedListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
    
    def __init__(self):
        self.head = None
        self.length = 0

    def get(self, index: int) -> int:
        if index > self.length-1:
            return -1
        currIndex = 0
        curr = self.head
        while currIndex != index:
            curr = curr.next
            currIndex+=1
        return curr.val

    def insertHead(self, val: int) -> None:
        oldHead = self.head
        newHead = self.LinkedListNode(val, oldHead)
        self.head = newHead
        self.length += 1      

    def insertTail(self, val: int) -> None:
        if self.head == None:
            self.insertHead(val)
        else:
            curr = self.head
            prev = None
            while curr != None:
                prev = curr
                curr = curr.next
            newTail = self.LinkedListNode(val)
            prev.next = newTail
            self.length += 1
        
    def remove(self, index: int) -> bool:
        if index < 0 or index > self.length - 1:
            return False
        currIndex = 0
        prev = None
        curr = self.head
        while currIndex != index:
            prev = curr
            curr = curr.next
            currIndex+=1
        if prev == None:
           self.head = curr.next
        else:
            prev.next = curr.next
        self.length -= 1
        return True       

    def getValues(self) -> List[int]:
        output = []
        curr = self.head
        while curr != None:
            output.append(curr.val)
            curr = curr.next
        return output

        
