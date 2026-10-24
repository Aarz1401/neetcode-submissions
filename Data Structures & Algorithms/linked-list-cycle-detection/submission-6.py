# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p1 = head
        p2 = head

        if(head == None):
            return False
        if(head.next == None):
            return False

        while(p2 and p2.next != None):
            p1 = p1.next
            p2 = p2.next.next
            if(p2 == None):
                return False
            if(p1.val == p2.val):
                return True
        
        return False


        