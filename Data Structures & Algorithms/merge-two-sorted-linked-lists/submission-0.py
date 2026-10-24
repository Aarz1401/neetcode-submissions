# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #first create head
        MyNode = ListNode()
        head = MyNode
        curr = MyNode

        while(list1 and list2):
            if(list1.val < list2.val):
                curr.next = ListNode(list1.val)
                curr = curr.next
                list1 = list1.next
            else:
                curr.next = ListNode(list2.val)
                curr = curr.next
                list2 = list2.next
        
         # Append the remaining elements from whichever list isn't empty
        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2

        return head.next





        
        