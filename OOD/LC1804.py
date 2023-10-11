class Trie:
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.cnt = 0
            self.cnt_start_with = 0

    def __init__(self):
        self.root = self.TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = self.TrieNode()
            curr.cnt_start_with += 1
            curr = curr.children[ch]
        curr.cnt += 1
            

    def countWordsEqualTo(self, word: str) -> int:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                return 0
            curr = curr.children[ch]
        return curr.cnt
        

    def countWordsStartingWith(self, prefix: str) -> int:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                return 0
            curr = curr.children[ch]
        return curr.cnt_start_with
        

    def erase(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                return
            curr = curr.children[ch]
            curr.cnt_start_with -= 1
        if curr.cnt > 0:
            curr.cnt -= 1

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)