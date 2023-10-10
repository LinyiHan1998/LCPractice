
class LRUCache:
    class Node:
        def __init__(self,k,v):
            self.key = k
            self.value = v
            self.prev = None
            self.next = None


    def __init__(self, capacity: int):
        self.head = self.Node(0,0)
        self.tail = self.Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.map = {}
            
    def addNode(self,x):
        x.prev = self.tail.prev
        x.next = self.tail
        self.tail.prev.next = x
        self.tail.prev = x

    def remove(self,x):
        x.prev.next = x.next
        x.next.prev = x.prev

    def get(self, key: int) -> int:
        if key in self.map:
            x = self.map[key]
            del self.map[key]
            self.remove(x)
            self.addNode(x)
            self.map[key] = self.tail.prev
            return x.value
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            x = self.map[key]
            del self.map[key]
            self.remove(x)
        if len(self.map) == self.capacity:
            del self.map[self.head.next.key]
            self.remove(self.head.next)
        x = self.Node(key,value)
        self.addNode(x)
        self.map[key] = self.tail.prev

            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)