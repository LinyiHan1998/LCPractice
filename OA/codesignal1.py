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

    def pay(self, timestamp, account_id, amount):
        if account_id not in self.account:
            return ""
        bal = self.account[account_id]
        if bal < int(amount):
            return ""
        self.account[account_id] -= int(amount)
        self.transactions[account_id] += int(amount)
        return str(self.account[account_id])

    def top_activity(self, timestamp, n):
        n = int(n)
        sz = len(self.transactions)
        hm = sorted(self.transactions.items(), key=lambda kv: -1 * kv[1])
        res = []
        for i in range(min(n, sz)):
            res.append(str(hm[i][0]) + '(' + str(hm[i][1]) + ')' + ' ')

        return ', '.join(res)

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


def solution(queries):
    bank = Bank()
    res = []
    for query in queries:
        if query[0] == 'CREATE_ACCOUNT':
            res.append(bank.create_account(query[1], query[2]))
        elif query[0] == 'DEPOSIT':
            res.append(bank.deposit(query[1], query[2], query[3]))
        elif query[0] == 'PAY':
            res.append(bank.pay(query[1], query[2], query[3]))

        elif query[0] == 'TOP_ACTIVITY':
            res.append(bank.top_activity(query[1], query[2]))
        elif query[0] == 'TRANSFER':
            res.append(bank.transfer(query[1], query[2], query[3], query[4]))
        elif query[0] == 'ACCEPT_TRANSFER':
            res.append(bank.accept_transfer(query[1], query[2], query[3]))
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