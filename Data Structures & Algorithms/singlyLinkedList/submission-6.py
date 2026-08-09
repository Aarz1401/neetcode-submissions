class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    
    def get(self, index: int) -> int:
        if(index >= self.count):
            return -1
        current = self.head
        for i in range(index):
            current = current.next
        return current.val



    def insertHead(self, val: int) -> None:
        newNode = ListNode(val)
        if(self.count == 0):
            self.head = newNode
            self.count += 1
            return
        else :
            newNode.next = self.head
            self.head = newNode
            self.count += 1

    def insertTail(self, val: int) -> None:
        newNode = ListNode(val)
        if(self.count == 0):
            self.head = newNode
            self.count += 1
            return
        current = self.head
        while (current.next):
            current = current.next
        # current points to tail
        current.next = newNode
        self.count += 1
        

    def remove(self, index: int) -> bool:
        if(index >= self.count):
            return False
        if(index == 0):
            self.head = self.head.next
            self.count = self.count - 1 
            return True
        current = self.head
        for i in range(index - 1):
            current = current.next
        #now current points to element before the one we want to remove
        current.next = current.next.next
        self.count = self.count - 1
        return True


    def getValues(self) -> List[int]:
        arr = []
        current = self.head
        while(current):
            arr.append(current.val)
            current= current.next
        return arr
