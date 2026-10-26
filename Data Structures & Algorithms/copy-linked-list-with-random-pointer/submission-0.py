"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        myMap = {None : None}
        temp = head
        while(head):
            copy = Node(head.val)
            myMap[head] = copy
            head = head.next
        head = temp
        temp = head
        while(head):
            copy = myMap[head]
            copy.next = myMap[head.next]
            copy.random = myMap[head.random]
            head = head.next
        return myMap[temp]
        
            