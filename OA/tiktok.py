def p5(packets, max_frame):
    n = len(packets)
    max_val = float('-inf')
    min_val = float('inf')

    for i in range(n):
        if packets[i] == 0:
            continue
        if (i > 0 and packets[i - 1] == 0) or (i < n - 1 and packets[i + 1] == 0):
            max_val = max(max_val, packets[i])
            min_val = min(min_val, packets[i])

    if max_val == float('-inf') and min_val == float('inf'):
        return max([abs(packets[i] - packets[i-1]) for i in range(1, n)], default=0)

    replace_val = min((int(max_val) + int(min_val)) // 2, max_frame)
    return max(max_val - replace_val, replace_val - min_val)


def p4(words):
    hm = {chr(ord('a') + i): i for i in range(26)}
    result = ""
    for i in range(len(words[0])):
        mid = 0
        for j in range(len(words)):
            mid += hm[words[j][i]] + hm[words[j][-i-1]]
        result += chr(ord('a') + mid // (len(words) * 2))
    return result