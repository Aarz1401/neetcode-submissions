class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    
    def get(self, index: int) -> int:
        if (index >= self.count):
            return -1
        else :
            target = self.head
            for i in range(index):
                target = target.next
            return target.val

    def insertHead(self, val: int) -> None:
        newNode = ListNode(val, self.head)
        self.head = newNode
        if self.count == 0:
            self.tail = newNode
        self.count = self.count + 1

    def insertTail(self, val: int) -> None:
        newNode = ListNode(val)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.count = self.count + 1

    def remove(self, index: int) -> bool:
        if (index >= self.count):
            return False
        if index == 0:
            self.head = self.head.next
            if self.count == 1:
                self.tail = None
        else:
            beforetarget = self.head
            for i in range(index - 1):
                beforetarget = beforetarget.next
            beforetarget.next = beforetarget.next.next
            if index == self.count - 1:
                self.tail = beforetarget
        self.count = self.count - 1
        return True

    def getValues(self) -> List[int]:
        arr = []
        curr = self.head
        for i in range(self.count):
            if(curr != None):
                arr.append(curr.val)
                curr = curr.next
        return arr