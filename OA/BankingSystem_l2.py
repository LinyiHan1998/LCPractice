class Bank:
    def __init__(self) -> None:
        self.account = {}
        self.transactionsValue={}
    def CREATE_ACCOUNT(self,timestamp,accountId):
        if accountId in self.account:
            return "false"
        self.account[accountId] = 0
        self.transactionsValue[accountId] = 0
        return "true"
    def DEPOSIT(self,timestamp,accountId,amount):
        if accountId not in self.account:
            return ""
        self.account[accountId] += int(amount)
        self.transactionsValue[accountId] += int(amount)
        return str(self.account[accountId])
    def PAY(self,timestamp,accountId,amount):
        if accountId not in self.account:
            return ""
        bal = self.account[accountId]
        if bal < int(amount):
            return ""
        self.account[accountId] = bal - int(amount)
        self.transactionsValue[accountId] += int(amount)
        return str(self.account[accountId])
    def TOP_ACTIVITY(self,timestamp,num):
        n = int(num)
        sz = len(self.transactionsValue)

        dict1 = sorted(self.transactionsValue.items(), key = lambda kv:-1*kv[1])

        res = []
        if sz <= n:
            for key,value in dict1:
                res.append(key+'('+str(value)+')'+'')
        else:
            for i in range(n):
                res.append(dict1[i][0]+'('+str(dict1[i][1])+')'+' ')
        
        return ', '.join(res)


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
        elif query[0] == 'TOP_ACTIVITY':
            res.append(bank.TOP_ACTIVITY(query[1],query[2]))
    return res

if __name__=='__main__':
    queries1 =[
        ["CREATE_ACCOUNT","1","account1"],
        ["CREATE_ACCOUNT","2","account1"],
        ["CREATE_ACCOUNT","3","account2"],
        ["DEPOSIT","4","non-existing","2700"],
        ["DEPOSIT","5","account1","2700"],
        ["PAY","6","non-existing","2700"],
        ["PAY","7","account1","2701"],
         ["PAY","8","account1","200"]
        ]
    queries2 =[
        ["CREATE_ACCOUNT","1","account1"],
        ["CREATE_ACCOUNT","2","account2"],
        ["CREATE_ACCOUNT","3","account3"],
        ["DEPOSIT","4","account1","2000"],
        ["DEPOSIT","5","account2","3000"],
        ["DEPOSIT","6","account3","4000"],
        ["TOP_ACTIVITY","7","3"],
        ["PAY","8","account1","1500"],
        ["PAY","9","account2","250"],
        ["DEPOSIT","10","account3","250"],
        ["TOP_ACTIVITY","11","3"],
        ]
    
    print(solution(queries2))