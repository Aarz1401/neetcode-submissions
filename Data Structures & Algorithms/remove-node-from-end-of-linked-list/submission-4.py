# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node_arr = []
        temp = head
        while(head):
            node_arr.append(head)
            head = head.next
        target_idx = len(node_arr) - n
        if(len(node_arr) == 1):
            return None
        if(target_idx == 0):
            temp = temp.next
            return temp
        if(n == 1):
            node_arr[target_idx - 1].next = None
            return temp
        node_arr[target_idx-1].next = node_arr[target_idx+1]
        node_arr[target_idx].next = None

        return temp
