class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.end = True
    def findPrefix(self,prefix):
        curr = self.root
        res = ''
        for ch in prefix:
            if ch in curr.children and curr.children[ch].end != True:
                curr = curr.children[ch]
                res += ch
            elif ch in curr.children and curr.children[ch].end == True:
                res += ch
                return res
            else:
                return ''
        return ''

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        sentences = sentence.split(' ')

        tree = Trie()
        for word in dictionary:
            tree.insert(word)
        res = ''
        for sen in sentences:
            tmp = tree.findPrefix(sen)
            if tmp == '':
                res += sen
            else:
                res += tmp
            res += ' '
        return res.strip()
        