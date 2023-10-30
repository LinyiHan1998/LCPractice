class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList or not wordList or not endWord or not beginWord:
            return 0
        L = len(beginWord)
        all_word = defaultdict(list)

        for word in wordList:
            for i in range(L):
                all_word[word[:i]+'*'+word[i+1:]].append(word)
        que = deque([(beginWord,1)])
        visited = set()
        visited.add(beginWord)
        while que:
            curr_word,level = que.popleft()
            for i in range(L):
                middle = curr_word[:i] + '*' + curr_word[i+1:]
                for word in all_word[middle]:
                    if endWord == word:
                        return level + 1
                    if word not in visited:
                        visited.add(word)
                        que.append((word,level+1))
        return 0
            
        