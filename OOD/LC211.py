class WordDictionary:
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.end = False

    def __init__(self):
        self.root = self.TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = self.TrieNode()
            curr = curr.children[ch]
        curr.end = True

        

    def search(self, word: str) -> bool:
        def dfs(node,idx):
            if idx == len(word):
                return node.end
            if word[idx] == '.':
                for child in node.children.values():
                    if dfs(child,idx+1):
                        return True
            if word[idx] in node.children:
                return dfs(node.children[word[idx]],idx+1)
            return False
        return dfs(self.root,0)
            
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)