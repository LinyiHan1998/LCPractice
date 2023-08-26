class solution:
    def __init__(self) -> None:
        self.hold={}
        self.price={}
        self.query=[]
    def Buy(self,stockName,stockQuant):
        if stockName not in self.hold:
            self.hold[stockName] = stockQuant
        else:
            self.hold[stockName] += stockQuant
        if stockName not in self.price:
            self.price[stockName] = 0
    def Sell(self,stockName,stockQuant):
        self.hold[stockName] -= stockQuant
    def Change(self,stockName,change):
        self.price[stockName] += change
    def Query(self):
        
        q = 0
        if self.query:
            q = self.query[-1]
        for item in self.hold:
            if self.price[item] != 0:
                q += self.price[item] * self.hold[item]
                self.price[item] = 0
        self.query.append(q)
        return self.query

if __name__ == '__main__':
    s = solution()
    s.Buy('a',20)
    s.Buy('b',50)
    print(s.hold)
    print(s.price)
    s.Change('a',6)
    print(s.Query())
    s.Sell('b',10)
    s.Change('b',-2)
    print(s.Query())
