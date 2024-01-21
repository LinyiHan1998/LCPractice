






def p3(n, total_bandwidth: int, bandwidth: List, request: List):
    m = total_bandwidth
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if j < bandwidth[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - bandwidth[i - 1]] + request[i - 1])

    return dp[n][m]


def p4(timestamps, messages, k ):
    hm = {}
    res = []
    for i, msg in enumerate(messages):
        if msg in hm:
            if timestamps[i] >= hm[msg] + k:
                res.append('true')
            else:
                res.append('false')
        else:
            res.append('true')
        hm[msg] = timestamps[i] 

    return res


def p5(n: int, memory: List):
    left, right = 0, len(memory) - 1
    while left < right:
        if memory[left] > memory[right]:
            memory[left], memory[right] = memory[right], memory[left]
        left, right = left + 1, right - 1
    total = sum([(i + 1) * memory[i] for i in range(n)]) % (10 ** 9 + 7)
    return total