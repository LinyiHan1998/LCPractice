class Bank:
    def __init__(self) -> None:
        self.account = {}
        self.transactionsValue={}
        self.transfer = {} #transferId : [sourceacc,targetacc,amount,expiretime]
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
    def TRANSFER(self,timestamp,sourceAccountId,targetAccountId,amount):
        amt = int(amount)
        if sourceAccountId == targetAccountId:
            return ""
        elif sourceAccountId not in self.account or targetAccountId not in self.account:
            return ""
        bal = self.account[sourceAccountId]
        if bal<amt:
            return ""
        idx = str(len(self.transfer)+1)
        transferId = 'transfer'+idx
        self.transfer[transferId] = [sourceAccountId,targetAccountId,amount,int(timestamp)+86400000]
        print(self.transfer.items())
        self.account[sourceAccountId] -= int(amount)
        return transferId
    def ACCEPT_TRANSFER(self,timestamp,accountId,transferId):
        for transaction in self.transfer:
            if timestamp > transaction[3] and transaction[3] != -1 :
                self.account[transaction[0]] += int(transaction[2])
                transaction[3] = -1
        if transferId not in self.transfer:
            return "false"
        if accountId != self.transfer[transferId][1]:
            return "false"
        if int(timestamp) > self.transfer[transferId][3]:
            return "false"
        self.account[accountId] += int(self.transfer[transferId][2])
        self.transactionsValue[accountId] += int(self.transfer[transferId][2])
        self.transactionsValue[self.transfer[transferId][0]] += int(self.transfer[transferId][2])
        self.transfer[transferId][3] = -1
        return "true"


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
        elif query[0] == 'TRANSFER':
            res.append(bank.TRANSFER(query[1],query[2],query[3],query[4]))
        elif query[0] == 'ACCEPT_TRANSFER':
            res.append(bank.ACCEPT_TRANSFER(query[1],query[2],query[3]))
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
    
    queries3 = [
    ["CREATE_ACCOUNT", "1", "account1"],
    ["CREATE_ACCOUNT", "2", "account2"],
    ["DEPOSIT", "3", "account1", 2000],
    ["DEPOSIT", "4", "account2", 3000],
    ["TRANSFER", "5", "account1", "account2", 5000],
    ["TRANSFER", "16", "account1", "account2", 1000],
    ["ACCEPT_TRANSFER", "20", "account1", "transfer1"],
    ["ACCEPT_TRANSFER", "21", "non-existing", "transfer1"],
    ["ACCEPT_TRANSFER", "22", "account1", "transfer2"],
    ["ACCEPT_TRANSFER", "25", "account2", "transfer1"],
    ["ACCEPT_TRANSFER", "30", "account2", "transfer1"],
    ["TRANSFER", "40", "account1", "account2", 1000],
    ["ACCEPT_TRANSFER", "86400045", "account2", "transfer2"],
    ["TRANSFER", "86400050", "account1", "account1", 1000],
]
    
    print(solution(queries3))