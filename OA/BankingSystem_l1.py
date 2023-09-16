class Bank:
    def __init__(self) -> None:
        self.account = {}
    def CREATE_ACCOUNT(self,timestamp,accountId):
        if accountId in self.account:
            return "false"
        self.account[accountId] = 0
        return "true"
    def DEPOSIT(self,timestamp,accountId,amount):
        if accountId not in self.account:
            return ""
        self.account[accountId] += int(amount)
        return str(self.account[accountId])
    def PAY(self,timestamp,accountId,amount):
        if accountId not in self.account:
            return ""
        bal = self.account[accountId]
        if bal < int(amount):
            return ""
        self.account[accountId] = bal - int(amount)
        return str(self.account[accountId])

def solution(queries):
    bank = Bank()
    res = []
    for query in queries:
        if query[0] == 'CREATE_ACCOUNT':
            res.append(bank.CREATE_ACCOUNT(query[1],query[2]))
        elif query[0] == 'DEPOSIT':
            res.append(bank.DEPOSIT(query[1],query[2],query[3]))
        elif query[0] == 'PAY':
            res.append(bank.PAY(query[1],query[2],query[3]))
    return res

if __name__=='__main__':
    queries =[
        ["CREATE_ACCOUNT","1","account1"],
        ["CREATE_ACCOUNT","2","account1"],
        ["CREATE_ACCOUNT","3","account2"],
        ["DEPOSIT","4","non-existing","2700"],
        ["DEPOSIT","5","account1","2700"],
        ["PAY","6","non-existing","2700"],
        ["PAY","7","account1","2701"],
         ["PAY","8","account1","200"]
        ]
    print(solution(queries))