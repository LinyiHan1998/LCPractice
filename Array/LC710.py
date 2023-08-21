def __init__(self, n: int, blacklist: List[int]):

    self.sz = n - len(blacklist)
    self.map = {}
    for b in blacklist:
        self.map[b] = 1
    last = n-1
    for b in blacklist:
        if b >= self.sz:
            continue
        while last in self.map:
            last -= 1
        self.map[b] = last
        last -= 1
    

def pick(self) -> int:
    idx = random.randint(0,self.sz-1)
    if idx in self.map:
        return self.map[idx]
    return idx