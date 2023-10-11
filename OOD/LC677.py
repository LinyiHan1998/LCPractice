class MapSum:
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.cnt_start_with = 0

    def __init__(self):
        self.root = self.TrieNode()
        self.dict = {}
        

    def insert(self, key: str, val: int) -> None:
        curr = self.root
        delta = val
        if key in self.dict:
            delta -= self.dict[key]
        self.dict[key] = val
        for ch in key:
            if ch not in curr.children:
                curr.children[ch] = self.TrieNode()
            curr = curr.children[ch]
            curr.cnt_start_with += delta        

    def sum(self, prefix: str) -> int:
        curr = self.root
        for ch in prefix:
            if ch not in curr.children:
                return 0
            curr = curr.children[ch]
        return curr.cnt_start_with
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)