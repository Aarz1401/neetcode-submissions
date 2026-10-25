# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = []
        curr = head
        while(head):
            nodes.append(head)
            head = head.next
        front = 0 
        back = len(nodes) - 1
        while(front < back):
            nodes[front].next = nodes[back]
            front = front + 1
            '''if(front >= back):
                break '''
            nodes[back].next = nodes[front]
            back = back - 1

        nodes[front].next = None

        
