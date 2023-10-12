class Solution:
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.end = False
    class Trie:
        def __init__(self):
            self.root = Solution.TrieNode()
            self.res = []
        def insert(self,word):
            node = self.root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = Solution.TrieNode()
                node = node.children[ch]
            node.end = True
        def search(self,word,path):
            if not word:
                self.res.append("".join(path).strip())
                return
            node = self.root
            for i ,w in enumerate(word):
                path.append(w)
                if w not in node.children:
                    return
                if node.children[w].end:
                    self.search(word[i+1:],path+[" "])
                node = node.children[w]

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        trie = self.Trie()
        for word in wordDict:
            trie.insert(word)
        trie.search(s,[])
        return trie.res