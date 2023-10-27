class MyLinkedList:
    class Node:
        def __init__(self):
            self.val = 0
            self.next = None
            self.prev = None

    def __init__(self):
        self.head = self.Node()
        self.tail = self.Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, index: int) -> int:
        if self.size <= index or index < 0:
            return -1
        curr = self.findIndex(index)
        return curr.val
        

    def addAtHead(self, val: int) -> None:
        curr = self.Node()
        curr.val = val
        curr.next = self.head.next
        curr.prev = self.head
        self.head.next.prev = curr
        self.head.next = curr
        self.size += 1

        

    def addAtTail(self, val: int) -> None:
        curr = self.Node()
        curr.val = val
        curr.prev = self.tail.prev
        curr.next = self.tail
        self.tail.prev.next = curr
        self.tail.prev = curr
        self.size += 1

    def findIndex(self,index):
        p = self.head
        i = -1
        while i<index:
            p = p.next
            i += 1
        return p

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        elif index == 0:
            self.addAtHead(val)
            return 
        elif index == self.size:
            self.addAtTail(val)
            return

        curr = self.findIndex(index)
        node = self.Node()
        node.val = val

        curr.prev.next = node
        node.prev = curr.prev

        node.next = curr
        curr.prev = node

        self.size += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size or index < 0:
            return None
        curr = self.findIndex(index)
        curr.prev.next = curr.next
        if curr.next:
            curr.next.prev = curr.prev
        curr.prev = None
        curr.next = None

        self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)