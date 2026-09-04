# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        prev = None
        curr = head
        ahead = head
        i = 0
        while i < n:
            ahead = ahead.next
            i+=1
        while ahead:
            prev = curr
            curr = curr.next
            ahead = ahead.next
        
        if curr == head:
            head = curr.next
        elif not curr.next:
            prev.next = None
        else:
            prev.next = curr.next
        return head
        
        
        
        
            
        