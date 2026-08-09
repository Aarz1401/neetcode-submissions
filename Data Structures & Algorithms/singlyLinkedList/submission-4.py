class ListNode:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.count = 0

    def get(self, index: int) -> int:
        if (index >= self.count):
            return -1
        current = self.head
        for i in range(index):
            current = current.next
        return current.value


    def insertHead(self, val: int) -> None:
        newNode = ListNode(val)
        if(self.count == 0):
            self.head = newNode
            self.count += 1
        else:
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
        current.next = newNode
        self.count += 1
        

    def remove(self, index: int) -> bool:
        current = self.head
        if(index >= self.count):
            return False
        if (index == 0):
            self.head = self.head.next
            self.count -= 1
            return True
        for i in range(index - 1):
            current = current.next
        current.next = current.next.next
        self.count -= 1
        return True
        
        

    def getValues(self) -> List[int]:
        arr =[]
        current = self.head
        for i in range(self.count):
            arr.append(current.value)
            current = current.next
        return arr


        
