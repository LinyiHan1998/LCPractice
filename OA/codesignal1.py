






#都没看到题目要哪个函数
class Bank:
    def __init__(self) -> None:
        self.account = {} # id: deposit
        self.transactions = {} # id: transactions
        self.transfer_id = 0
        self.transfer_event = {} # id: {'timestamp':timestamp, 'source':source, 'target':target, 'amount':amount, 'flag'}

    def create_account(self, timestamp, account_id):
        if account_id in self.account:
            return "false"
        self.account[account_id] = 0
        self.transactions[account_id] = 0
        return "true"

    def deposit(self, timestamp, account_id, amount):
        if account_id not in self.account:
            return ""
        self.account[account_id] += int(amount)
        self.transactions[account_id] += int(amount)
        return str(self.account[account_id])
##  level4 很难，为啥要自己想，自己想的话提前准备是为啥呢
    def pay(self, timestamp, account_id, amount):#谁知道啊，不是你现在做的这个题啊。你现在做的不是要找到动账最多的吗，不就是top activity吗。你现在看的不还是level1的需求吗
        if account_id not in self.account:
            return ""
        bal = self.account[account_id]
        if bal < int(amount):
            return ""
        self.account[account_id] -= int(amount)
        self.transactions[account_id] += int(amount)
        return str(self.account[account_id])

    def top_activity(self, timestamp, n): #不就是这个函数吗，我第一次就给你看了这里啊
        n = int(n)
        sz = len(self.transactions)
        hm = sorted(self.transactions.items(), key=lambda kv: -1 * kv[1])
        res = []
        for i in range(min(n, sz)):
            res.append(str(hm[i][0]) + '(' + str(hm[i][1]) + ')' + ' ')

        return ', '.join(res)
    #solution q[1]写成了1【1
    def schedule_payment(self,timestamp,accountId,amount,delay):
        pass
    #感觉差不多


    def transfer(self, timestamp, source_account_id, target_account_id, amount):
        if source_account_id == target_account_id:
            return ""

        if source_account_id not in self.account or target_account_id not in self.account:
            return ""

        if self.account[source_account_id] < amount:
            return ""

        self.transfer_id += 1
        cur_transfer_id = "transfer" + str(self.transfer_id)
        self.transfer_event[cur_transfer_id] = {
            "timestamp": timestamp,
            "source": source_account_id,
            "target": target_account_id,
            "amount": amount,
            "flag": 0
        }

        return cur_transfer_id
    #每个函数都要加对时间戳的处理
    #时间到了要给到点的扣钱
    #那个schedule的到了13也要扣钱了，错在了没扣schedule的余额，而且要先扣schedule的再加deposit的
    
    def timeup(self,timestamp):
        for transaction in self.transfer:#按你的改呀，我不知道你写的是啥，你每次画那么快看不到，
            #拿timestamp和你的字典里的expire比
            #判断等于把，不用小于，等于的时候执行扣钱
            #那也是timestamp > expire吧
            #每个函数执行的时候都要走一下timeup
            #self.

            #要是一次略过了很多比交易怎么办
            #要不要根据时间排个序，先expire的先扣钱
            #扣完钱的把expire改成inf
            #sorted dict lambda拿个搞搞不可以 lambda x : x[1]["exipre"]么
            #都没有hidden test case岂不是可以写死
            #cancel的漏了

            #怎么感觉每次都加了呀
            #是不是没判断已经加过了不加
            if timestamp > transaction[3] and transaction[3] != -1 :
                self.account[transaction[0]] += int(transaction[2])
                transaction[3] = -1
    def accept_transfer(self, timestamp, account_id, transfer_id):
        if transfer_id not in self.transfer_event:
            return "false"
        if account_id != self.transfer_event[transfer_id]["target"]:
            return "false"
        if int(timestamp) > int(self.transfer_event[transfer_id]["timestamp"]) + 86400000:
            return "false"
        if self.transfer_event[transfer_id]["flag"] == 1:
            return "false"

        self.transfer_event[transfer_id]["flag"] = 1
        self.transactions[self.transfer_event[transfer_id]["source"]] += self.transfer_event[transfer_id]["amount"]
        self.transactions[self.transfer_event[transfer_id]["target"]] += self.transfer_event[transfer_id]["amount"]

        return "true"
    def merge_account(self,timestamp,acc1,acc2):
        if acc1 == acc2:
            pass
        self.account[acc1] += self.account[acc2]
        # self.payment[cur_transfer_id] = {
        #     "timestamp": timestamp,
        #     "source": source_account_id,
        #     "target": target_account_id,
        #     "amount": amount,
        #     "flag": 0
        # }

        ##就把source也变成acc1试试，不行再说，能过几个是几个
        for transaction in self.payment :
            if target == acc2:
                target = acc1
    def get_balance(self,timestamp,account_id,time_at):
        cur_balance = self.account(account_id)

        time_dict = {} #schedule且没被cancel，且source或者target是自己的时间戳：schedule的金额，是source就是负数，是target就是正数
        #先把merge的跑了吧，能过几个testcase也加分
        #solution写了吗
        #看看别的error
        #没删self.account 里被合并的账号
        for pay in self.payment_event:
            time_dict[pay["expire"]] = pay["amount"]
        sorted_dict = dict(sorted(time_dict.items()))



def solution(queries):
    bs = Bank()
    res = []
    for q in queries:
        if q[0] == 'CREATE_ACCOUNT':
            res.append(bs.create_account(q[1], q[2]))
        elif q[0] == 'DEPOSIT':
            res.append(bs.deposit(q[1], q[2], q[3]))
        elif q[0] == 'PAY':
            res.append(bs.pay(q[1], q[2], q[3]))

        elif q[0] == 'TOP_ACTIVITY':
            res.append(bs.top_activity(q[1], q[2]))
        elif q[0] == 'TRANSFER':
            res.append(bs.transfer(q[1], q[2], q[3], q[4]))
        elif q[0] == 'ACCEPT_TRANSFER':
            res.append(bs.accept_transfer(q[1], q[2], q[3]))
    return res


if __name__ == '__main__':
    queries1 = [
        ["CREATE_ACCOUNT", "1", "account1"],
        ["CREATE_ACCOUNT", "2", "account1"],
        ["CREATE_ACCOUNT", "3", "account2"],
        ["DEPOSIT", "4", "non-existing", "2700"],
        ["DEPOSIT", "5", "account1", "2700"],
        ["PAY", "6", "non-existing", "2700"],
        ["PAY", "7", "account1", "2701"],
        ["PAY", "8", "account1", "200"]
    ]
    queries2 = [
        ["CREATE_ACCOUNT", "1", "account1"],
        ["CREATE_ACCOUNT", "2", "account2"],
        ["CREATE_ACCOUNT", "3", "account3"],
        ["DEPOSIT", "4", "account1", "2000"],
        ["DEPOSIT", "5", "account2", "3000"],
        ["DEPOSIT", "6", "account3", "4000"],
        ["TOP_ACTIVITY", "7", "3"],
        ["PAY", "8", "account1", "1500"],
        ["PAY", "9", "account2", "250"],
        ["DEPOSIT", "10", "account3", "250"],
        ["TOP_ACTIVITY", "11", "3"],
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